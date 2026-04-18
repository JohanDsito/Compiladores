grammar Saludo;

saludo: 'hola' NOMBRE ;

NOMBRE: [A-Z][a-z]+ ;
WS: [ \t\r\n]+ -> skip ;