grammar Numeros;

numero: NUMERO | LETRAS;

LETRAS: [a-zA-Z];
NUMERO: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;