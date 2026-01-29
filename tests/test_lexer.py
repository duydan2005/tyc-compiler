"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer

def test_lexer_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = "// This is a placeholder test"
    tokenizer = Tokenizer(source)
    # TODO: Add actual test assertions
    assert True

def test_lexer_01():
    source = "int a = 10;"
    expected = "INT,int,ID,a,ASSIGN,=,INTLIT,10,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected

def test_lexer_02():
    source = "string a=\"@@@@\";"
    expected= "STRING,string,ID,a,ASSIGN,=,STRINGLIT,@@@@,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected
    

def test_lexer_03():
    source = "a=a+b;"
    expected= "ID,a,ASSIGN,=,ID,a,PLUS,+,ID,b,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected

def test_lexer_04():
    source = "\"Hello World"
    expected= "Unclosed String: Hello World"
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value) == expected

def test_lexer_05():
    source = "/// Comment"
    expected= "EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected

def test_lexer_06():
    source = " "
    expected= "EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected

def test_lexer_07():
    source = "" \
    ""
    expected= "EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected 

def test_lexer_07():
    source = "while (i<=0){" \
    "i+=1;" \
    "}"
    expected= "WHILE,while,LPAR,(,ID,i,LE,<=,INTLIT,0,RPAR,),LBRACE,{,ID,i,PLUS,+,ASSIGN,=,INTLIT,1,SEMI,;,RBRACE,},EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected 

def test_lexer_08():
    source = "float a=.5;"
    expected= "FLOAT,float,ID,a,ASSIGN,=,FLOATLIT,.5,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected

def test_lexer_09():
    source = "float a=0.5+5e1;"
    expected= "FLOAT,float,ID,a,ASSIGN,=,FLOATLIT,0.5,PLUS,+,FLOATLIT,5e1,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected

def test_lexer_10():
    source = "if (i==1) return \"One\";"
    expected= "IF,if,LPAR,(,ID,i,EQ,==,INTLIT,1,RPAR,),RETURN,return,STRINGLIT,One,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected

def test_lexer_11():
    source = "@=123;"
    expected= "Error Token @"
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value) == expected

def test_lexer_12():
    source = "string a=\"Hello World\\n I'm Gnad!\";"
    expected= "STRING,string,ID,a,ASSIGN,=,STRINGLIT,Hello World\\n I'm Gnad!,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected

def test_lexer_13():
    source = "string a =\"Hello\nWorld\";"
    expected= "Unclosed String: Hello"
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value) == expected

def test_lexer_14():
    source = "string a = \"Hello\\qWord\";"
    expected= "Illegal Escape In String: Hello\\q"
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value) == expected

def test_lexer_15():
    source = "int a=2; \n " \
    "int b=3;\n" \
    "int c=b+a;"
    expected= "INT,int,ID,a,ASSIGN,=,INTLIT,2,SEMI,;,INT,int,ID,b,ASSIGN,=,INTLIT,3,SEMI,;,INT,int,ID,c,ASSIGN,=,ID,b,PLUS,+,ID,a,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected

def test_lexer_16():
    source = "int a=2; \n " \
    "int b=3;\n" \
    "int c=b+a;"
    expected= "INT,int,ID,a,ASSIGN,=,INTLIT,2,SEMI,;,INT,int,ID,b,ASSIGN,=,INTLIT,3,SEMI,;,INT,int,ID,c,ASSIGN,=,ID,b,PLUS,+,ID,a,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string()==expected

def test_lexer_17():
    source = "int x=10;"
    expected = "INT,int,ID,x,ASSIGN,=,INTLIT,10,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_18():
    source = "float y=3.14;"
    expected = "FLOAT,float,ID,y,ASSIGN,=,FLOATLIT,3.14,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_19():
    source = "string s=\"Hello\";"
    expected = "STRING,string,ID,s,ASSIGN,=,STRINGLIT,Hello,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_20():
    source = "if(a>=b) return a;"
    expected = (
        "IF,if,LPAR,(,ID,a,GE,>=,ID,b,RPAR,),"
        "RETURN,return,ID,a,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_21():
    source = "while(i<10) i++;"
    expected = (
        "WHILE,while,LPAR,(,ID,i,LT,<,INTLIT,10,RPAR,),"
        "ID,i,INC,++,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_22():
    source = "a=b+c*d;"
    expected = (
        "ID,a,ASSIGN,=,ID,b,PLUS,+,"
        "ID,c,MUL,*,ID,d,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_23():
    source = "a&&b||c"
    expected = (
        "ID,a,AND,&&,ID,b,OR,||,ID,c,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_24():
    source = "arr[2]=x;"
    expected = (
        "ID,arr,LBRACK,[,INTLIT,2,RBRACK,],ASSIGN,=,"
        "ID,x,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_25():
    source = "{int a; int b;}"
    expected = (
        "LBRACE,{,INT,int,ID,a,SEMI,;,INT,int,"
        "ID,b,SEMI,;,RBRACE,},EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_26():
    source = "/* comment */ int a;"
    expected = "INT,int,ID,a,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_27():
    source = "// line comment\nint a;"
    expected = "INT,int,ID,a,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_28():
    source = "a!=b;"
    expected = (
        "ID,a,NEQ,!=,ID,b,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_29():
    source = "x=1e+3;"
    expected = (
        "ID,x,ASSIGN,=,FLOATLIT,1e+3,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_30():
    source = "x=.5;"
    expected = (
        "ID,x,ASSIGN,=,FLOATLIT,.5,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_lexer_30():
    source = "int a=0;"
    expected = "INT,int,ID,a,ASSIGN,=,INTLIT,0,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_31():
    source = "int a=000;"
    expected = "INT,int,ID,a,ASSIGN,=,INTLIT,000,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_32():
    source = "float x=0.0;"
    expected = "FLOAT,float,ID,x,ASSIGN,=,FLOATLIT,0.0,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_33():
    source = "float x=.0;"
    expected = "FLOAT,float,ID,x,ASSIGN,=,FLOATLIT,.0,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_34():
    source = "float x=1e0;"
    expected = "FLOAT,float,ID,x,ASSIGN,=,FLOATLIT,1e0,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_35():
    source = "float x=1E-10;"
    expected = "FLOAT,float,ID,x,ASSIGN,=,FLOATLIT,1E-10,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_36():
    source = "_abc123=5;"
    expected = "ID,_abc123,ASSIGN,=,INTLIT,5,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_37():
    source = "a__b__c;"
    expected = "ID,a__b__c,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_38():
    source = "a+++b;"
    expected = (
        "ID,a,INC,++,PLUS,+,ID,b,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_39():
    source = "a----b;"
    expected = (
        "ID,a,DEC,--,DEC,--,ID,b,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_40():
    source = "a<=b>=c;"
    expected = (
        "ID,a,LE,<=,ID,b,GE,>=,ID,c,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_41():
    source = "string s=\"\";"
    expected = "STRING,string,ID,s,ASSIGN,=,STRINGLIT,,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_42():
    source = "string s=\"\\n\";"
    expected = "STRING,string,ID,s,ASSIGN,=,STRINGLIT,\\n,SEMI,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_43():
    source = "string s=\"hello \\t world\";"
    expected = (
        "STRING,string,ID,s,ASSIGN,=,"
        "STRINGLIT,hello \\t world,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_44():
    source = "string s=\"hello"
    expected="Unclosed String: hello"
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value)==expected


def test_lexer_45():
    source = "string s=\"hello\nworld\";"
    expected="Unclosed String: hello"
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value)==expected


def test_lexer_46():
    source = "string s=\"hello\\q\";"
    expected="Illegal Escape In String: hello\\q"
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value)==expected



def test_lexer_47():
    source = "// comment only"
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_48():
    source = "/* comment */"
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_49():
    source = "/* unclosed comment"
    expected = "DIV,/,MUL,*,ID,unclosed,ID,comment,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_50():
    source = "@"
    expected="Error Token @"
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value)==expected
def test_lexer_51():
    source = "+++"
    expected = "INC,++,PLUS,+,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_52():
    source = "---"
    expected = "DEC,--,MINUS,-,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_53():
    source = "a=b==c;"
    expected = (
        "ID,a,ASSIGN,=,ID,b,EQ,==,ID,c,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_54():
    source = "a=b!=c;"
    expected = (
        "ID,a,ASSIGN,=,ID,b,NEQ,!=,ID,c,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_55():
    source = "a=b<=c;"
    expected = (
        "ID,a,ASSIGN,=,ID,b,LE,<=,ID,c,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_56():
    source = "a=b>=c;"
    expected = (
        "ID,a,ASSIGN,=,ID,b,GE,>=,ID,c,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_57():
    source = "a=b<c;"
    expected = (
        "ID,a,ASSIGN,=,ID,b,LT,<,ID,c,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_58():
    source = "a=b>c;"
    expected = (
        "ID,a,ASSIGN,=,ID,b,GT,>,ID,c,SEMI,;,EOF"
    )
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_59():
    source = "a&&&&b"
    expected = "ID,a,AND,&&,AND,&&,ID,b,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_60():
    source = "a||||b"
    expected = "ID,a,OR,||,OR,||,ID,b,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_61():
    source = "123abc"
    expected = "INTLIT,123,ID,abc,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_62():
    source = "abc123def"
    expected = "ID,abc123def,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_63():
    source = "1.2.3"
    expected = "FLOATLIT,1.2,FLOATLIT,.3,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_64():
    source = "1e"
    expected = "INTLIT,1,ID,e,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_65():
    source = "1e+"
    expected = "INTLIT,1,ID,e,PLUS,+,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_66():
    source = "1e-"
    expected = "INTLIT,1,ID,e,MINUS,-,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_67():
    source = "\" \\\" \""
    expected = "STRINGLIT, \\\" ,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_68():
    source = "\"\\\\\""
    expected = "STRINGLIT,\\\\,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_69():
    source = "\"\\\"\""
    expected = "STRINGLIT,\\\",EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_70():
    source = "\"\\n\\t\\r\""
    expected = "STRINGLIT,\\n\\t\\r,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_71():
    source = "\"\\x\""
    expected = "Illegal Escape In String: \\x"
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value) == expected


def test_lexer_72():
    source = "\"abc\\\""
    expected = "Unclosed String: abc\\\""
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value) == expected


def test_lexer_73():
    source = "\"abc\\\\\""
    expected = "STRINGLIT,abc\\\\,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_74():
    source = "\"abc\\\n\""
    expected = "Illegal Escape In String: abc\\\n"
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value) == expected


def test_lexer_75():
    source = "/* /* nested */ */"
    expected = "MUL,*,DIV,/,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_76():
    source = "/* comment // still comment */"
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_77():
    source = "// /* comment */"
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_78():
    source = "_"
    expected = "ID,_,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_79():
    source = "__"
    expected = "ID,__,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_80():
    source = "___123"
    expected = "ID,___123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_81():
    source = "0x123"
    expected = "INTLIT,0,ID,x123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_82():
    source = "09"
    expected = "INTLIT,09,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_83():
    source = "."
    expected = "DOT,.,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_84():
    source = ".."
    expected = "DOT,.,DOT,.,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_85():
    source = "..."
    expected = "DOT,.,DOT,.,DOT,.,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_86():
    source = "\" \""
    expected = "STRINGLIT, ,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_87():
    source = "\"\" \"\""
    expected = "STRINGLIT,,STRINGLIT,,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_88():
    source = "\"a\"\"b\""
    expected = "STRINGLIT,a,STRINGLIT,b,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_89():
    source = "ifif"
    expected = "ID,ifif,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_90():
    source = "if if"
    expected = "IF,if,IF,if,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_91():
    source = "returnreturn"
    expected = "ID,returnreturn,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_92():
    source = "return return"
    expected = "RETURN,return,RETURN,return,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_93():
    source = "\"\\\"\""
    expected = "STRINGLIT,\\\",EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_94():
    source = "\"\\\\\\\"\""
    expected = "STRINGLIT,\\\\\\\",EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_95():
    source = "\"abc\\t\\nxyz\""
    expected = "STRINGLIT,abc\\t\\nxyz,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_96():
    source = "\"abc\\\"xyz\""
    expected = "STRINGLIT,abc\\\"xyz,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_97():
    source = "\"abc\\\""
    expected = "Unclosed String: abc\\\""
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value) == expected


def test_lexer_98():
    source = "\"abc\\z\""
    expected = "Illegal Escape In String: abc\\z"
    with pytest.raises(Exception) as e:
        Tokenizer(source).get_tokens_as_string()
    assert str(e.value) == expected


def test_lexer_99():
    source = "/*/"
    expected = "DIV,/,MUL,*,DIV,/,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_lexer_100():
    source = "/*"
    expected = "DIV,/,MUL,*,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected
