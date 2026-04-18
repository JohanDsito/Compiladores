grammar SumaResta;

expr: NUM op NUM ;

op: MAS | MENOS ;

MAS: '+';
MENOS: '-';

NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;