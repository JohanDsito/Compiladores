grammar Expr1;

expr: expr MAS NUM
    | NUM
    ;

MAS: '+';
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;