grammar Suma;

expr: NUM MAS NUM ;

MAS: '+';
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;