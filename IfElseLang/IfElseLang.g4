grammar IfElseLang;

program: statement+ EOF; 

declaration: type ID ('=' expr)? SEMI; 

type: INT_TYPE | STRING_TYPE;

statement
    : assignment
    | ifStatement
    | declaration
    ;

assignment: ID ASSIGN expr SEMI;

ifStatement
    : IF LPAREN condition RPAREN LBRACE statement* RBRACE
    (ELSE LBRACE statement* RBRACE)?
    ;

condition: expr;

expr
    : ID                                       # idExpr
    | NUMBER                                   # numberExpr
    | STRING                                   # stringExpr
    | expr (LT | GT | GE | LE | EQ | NE) expr  # comparisonExpr
    | expr (PLUS | MINUS | MUL | DIV) expr     # arithmeticExpr
    | LPAREN expr RPAREN                       # parenExpr
    ;

// === KEYWORDS ===
IF: 'if';
ELSE: 'else';
INT_TYPE: 'int';
STRING_TYPE: 'string';

// === SYMBOLS ===
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';

GE: '>=';
LE: '<=';
EQ: '==';
NE: '!=';

LT: '<';
GT: '>';

// === OPERADORES ===
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';

// === LITERALES ===
STRING: '"' (~["\r\n])* '"';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;

// === IGNORADOS ===
COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;