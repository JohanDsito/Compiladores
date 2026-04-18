grammar WhileLang;

program: statement+ EOF;

statement
    : declaration       # declStatement
    | assignment        # assignStatement
    | whileStatement    # whileStmt
    | ifStatement       # ifStmt
    | breakStatement    # breakStmt
    | continueStatement # continueStmt
    ;

declaration: type ID ASSIGN expr SEMI;

type: INT_TYPE | STRING_TYPE;

assignment: ID ASSIGN expr SEMI;

whileStatement: WHILE LPAREN condition RPAREN LBRACE statement* RBRACE;

ifStatement: IF LPAREN condition RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?;

breakStatement: BREAK SEMI;

continueStatement: CONTINUE SEMI;

condition
    : expr                              # exprCondition
    | expr (GT | LT | EQ | NE) expr    # comparisonCondition
    ;

expr
    : ID                                        # idExpr
    | NUMBER                                    # numberExpr
    | STRING                                    # stringExpr
    | expr (MULT | DIV) expr                    # arithmeticExpr
    | expr (PLUS | MINUS) expr                  # arithmeticExpr
    | LPAREN expr RPAREN                        # parenExpr
    ;

// Keywords
INT_TYPE    : 'int';
STRING_TYPE : 'string';
WHILE       : 'while';
IF          : 'if';
ELSE        : 'else';
BREAK       : 'break';
CONTINUE    : 'continue';

// Symbols
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
SEMI    : ';';
ASSIGN  : '=';

// Comparison operators
GT  : '>';
LT  : '<';
EQ  : '==';
NE  : '!=';

// Arithmetic operators
PLUS    : '+';
MINUS   : '-';
MULT    : '*';
DIV     : '/';

// Literals and identifiers
ID      : [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER  : [0-9]+;
STRING  : '"' (~["\r\n])* '"';
WS      : [ \t\r\n]+ -> skip;
