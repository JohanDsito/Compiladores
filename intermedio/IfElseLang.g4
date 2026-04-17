grammar IfElseLang;

program: (statement | functionDecl)+ EOF;

functionDecl: type ID LPAREN paramList? RPAREN block;
param: type ID;
paramList: param (',' param)*;

declaration: type ID ('=' expr)? SEMI; 

type: 'int' | 'string';

statement: assignment | ifStatement | declaration | returnStatement | expr SEMI;

returnStatement: 'return' expr SEMI;

assignment: ID ASSIGN expr SEMI;

ifStatement: IF LPAREN condition RPAREN block (ELSE block)?;

condition: expr; // ahora condición es cualquier expresión booleana

// Expresiones con etiquetas
expr
    : ID LPAREN argList? RPAREN               # funcCallExpr
    | ID                                       # idExpr
    | NUMBER                                   # numberExpr
    | STRING                                   # stringExpr    
    | expr (LT | GT | GE | LE | EQ | NE) expr  # comparisonExpr
    | expr (PLUS | MINUS | MUL | DIV) expr     # arithmeticExpr
    | LPAREN expr RPAREN                       # parenExpr
    ;

argList: expr (',' expr)*;

block: LBRACE statement* RBRACE;
IF: 'if';
ELSE: 'else';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';
LT: '<';
GT: '>';
GE: '>=';
LE: '<=';
EQ: '==';
NE: '!=';
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
STRING: '"' (~["\r\n])* '"';
COMMENT: '//' .*? '\n' -> skip;
WS: [ \t\r\n]+ -> skip;