grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// --- PARSER --- //

program: (struct_decl | func_decl)+ EOF;

// --- DECLARATIONS --- //
struct_decl: STRUCT ID LBRACE member_list RBRACE SEMI;
member_list: member_decl*;
member_decl: primitive_type ID SEMI;

func_decl: (primitive_type | VOID | AUTO)? ID LPAR param_list? RPAR block_statement;
param_list: param_decl (COMMA param_decl)*;
param_decl: primitive_type ID;

primitive_type: INT | FLOAT | STRING | ID;

// --- STATEMENTS --- //
statement
    : assign_statement SEMI         # AssignStmt
    | var_decl_stmt                 # VarDeclStmt
    | if_statement                  # IfStmt
    | while_statement               # WhileStmt
    | for_statement                 # ForStmt
    | switch_statement              # SwitchStmt
    | break_statement               # BreakStmt
    | continue_statement            # ContinueStmt
    | return_statement              # ReturnStmt
    | block_statement               # BlockStmt
    | expression SEMI               # ExprStmt // expression_statement
    ;

var_decl_stmt: (AUTO | primitive_type) ID (ASSIGN expression)? SEMI;

assign_statement: expr_or ASSIGN expression; 

if_statement: IF LPAR expression RPAR statement (ELSE statement)?;
while_statement: WHILE LPAR expression RPAR statement;

// For: init có thể là var decl hoặc assign stmt
for_statement
    : FOR LPAR for_init? SEMI expression? SEMI for_update? RPAR statement
    ;

// for_init chỉ chứa phần thân của khai báo hoặc gán, không chứa SEMI cuối
for_init
    : (AUTO | primitive_type) ID (ASSIGN expression)? // Khai báo biến
    | expr_or ASSIGN expression                       // Phép gán
    ;

// For Update: Bắt buộc là INC/DEC hoặc Assignment
// Sử dụng Stratified Rules để giới hạn chính xác
for_update
    : expr_postfix (INC | DEC)      # PostfixUpdate
    | (INC | DEC) expr_prefix       # PrefixUpdate
    | expr_or ASSIGN expression     # AssignUpdate
    ;

switch_statement: SWITCH LPAR expression RPAR LBRACE switch_body RBRACE;

switch_body
    : case_stmt+ default_stmt?
    | default_stmt
    | /* empty */ 
    ;

case_stmt: CASE expression COLON statement*; 
default_stmt: DEFAULT COLON statement*;

break_statement: BREAK SEMI;
continue_statement: CONTINUE SEMI;
return_statement: RETURN expression? SEMI;
block_statement: LBRACE statement* RBRACE;

// --- EXPRESSIONS (STRATIFIED) --- //

// Top-level: Assignment (Right Associative)
expression
    : expr_or ASSIGN expression     # AssignExpr
    | expr_or                       # OrExprPass
    ;

expr_or
    : expr_or OR expr_and           # OrExpr
    | expr_and                      # AndExprPass
    ;

expr_and
    : expr_and AND expr_eq          # AndExpr
    | expr_eq                       # EqExprPass
    ;

expr_eq
    : expr_eq (EQ | NEQ) expr_rel   # EqExpr
    | expr_rel                      # RelExprPass
    ;

expr_rel
    : expr_rel (LT | GT | LE | GE) expr_add  # RelExpr
    | expr_add                      # AddExprPass
    ;

expr_add
    : expr_add (PLUS | MINUS) expr_mult      # AddExpr
    | expr_mult                     # MultExprPass
    ;

expr_mult
    : expr_mult (MUL | DIV | MOD) expr_dot   # MultiExpr
    | expr_dot                      # DotExprPass
    ;

// Level 4: Member Access (Theo Spec: Thấp hơn Unary)
// Rule: expr_dot -> expr_dot . ID | expr_unary
// Điều này có nghĩa: !p.x sẽ được parse là (!p).x (Đúng Spec TyC)
expr_dot
    : expr_dot DOT ID               # MemberAccessExpr
    | expr_unary                    # UnaryExprPass
    ;

// Level 3: Unary (!, -, +)
// Rule này gọi xuống expr_prefix
expr_unary
    : (NOT | MINUS | PLUS) expr_unary   # UnaryExpr
    | expr_prefix                       # PrefixExprPass
    ;

// Level 2: Prefix (++, --)
// Rule này gọi xuống expr_postfix (Level 1)
// QUAN TRỌNG: Rule này KHÔNG gọi expr_unary. Do đó ++!a sẽ lỗi cú pháp.
expr_prefix
    : (INC | DEC) expr_prefix       # PrefixExpr
    | expr_postfix                  # PostfixExprPass
    ;

// Level 1: Postfix & Primary
expr_postfix
    : expr_postfix (INC | DEC)      # PostfixExpr
    | expr_primary                  # PrimaryExprPass
    ;

// Primary: ID, Literal, Function Call, (...)
expr_primary
    : ID LPAR (expression (COMMA expression)*)? RPAR # FuncCallExpr
    | ID                            # IdExpr
    | literal                       # LitExpr
    | LPAR expression RPAR          # ParenExpr
    ;

// --- LITERALS --- //
literal
    : INTLIT
    | FLOATLIT
    | STRINGLIT
    | struct_lit
    ;

struct_lit: LBRACE (expression (COMMA expression)*)? RBRACE;

// --- LEXER --- //

// TODO Keywords
AUTO        : 'auto';
BREAK       : 'break';
CASE        : 'case';
CONTINUE    : 'continue';
DEFAULT     : 'default';
ELSE        : 'else';
FLOAT       : 'float';
FOR         : 'for';
IF          : 'if';
INT         : 'int';
RETURN      : 'return';
STRING      : 'string';
STRUCT      : 'struct';
SWITCH      : 'switch';
VOID        : 'void';
WHILE       : 'while';

// TODO Operator
PLUS        : '+';
MINUS       : '-';
MUL         : '*';
DIV         : '/';
MOD         : '%';

EQ          : '==';
NEQ         : '!=';
LT          : '<';
GT          : '>';
LE          : '<=';
GE          : '>=';      

OR          : '||';
AND         : '&&';
NOT         : '!';

INC         : '++';
DEC         : '--';

ASSIGN      : '=';
DOT         : '.';

// TODO Separator
LBRACK      : '[';
RBRACK      : ']';
LBRACE      : '{';
RBRACE      : '}';
LPAR        : '(';
RPAR        : ')';
SEMI        : ';';
COMMA       : ',';
COLON       : ':';

// TODO Identifiers
ID          : LETTER (LETTER | DIGIT)*;

// TODO Literals
INTLIT      : '-'? DIGIT+;

FLOATLIT    : DIGIT+ '.' DIGIT* ([eE] [+-]? DIGIT+)?
            | '.' DIGIT+ ([eE] [+-]? DIGIT+)?
            | DIGIT+ [eE] [+-]? DIGIT+
            | '.' [eE] [+-]? DIGIT+
            | '-'
            ;

STRINGLIT   : '"' STR_CHAR* '"' {self.text = self.text[1:-1]};

// FRAGMENTS
fragment LETTER : [a-zA-Z_];
fragment DIGIT  : [0-9];
fragment ESC_SEQ: '\\' [bfnrt"\\];
fragment STR_CHAR : ~["\\\r\n] | ESC_SEQ;

// TODO Comment and WS
BLOCK_CMT   : '/*' .*? '*/' -> skip;
LINE_CMT    : '//' ~[\r\n]* -> skip;
WS: [ \t\r\n\f]+ -> skip;

// TODO ERROR
ILLEGAL_ESCAPE: '"' STR_CHAR* '\\' ~[bfnrt"\\];
UNCLOSE_STRING: '"' STR_CHAR* ('\r'? '\n' | '\r' | EOF);
ERROR_CHAR: .;

