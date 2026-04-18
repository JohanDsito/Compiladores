grammar ListaComas;

lista: NUMERO (COMA NUMERO)* ;

COMA: ',' ;
NUMERO: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;