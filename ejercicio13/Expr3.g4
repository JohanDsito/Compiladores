grammar Expr3;

expr: term ((MAS|MENOS) term)* ;

term: factor ((MUL|DIV) factor)* ;

factor: NUM ;

MAS: '+';
MENOS: '-';
MUL: '*';
DIV: '/';

NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;