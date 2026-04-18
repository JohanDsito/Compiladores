grammar Expr2;

prog: expr EOF;

expr: expr MAS expr
    | expr MUL expr
    | NUM
    ;

MAS: '+';
MUL: '*';

NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;