grammar Saludo2;

saludo: saludoTipo NOMBRE ;

saludoTipo
    : 'hola'
    | 'buenosdias'
    ;

NOMBRE: [A-Z][a-z]+ ;
WS: [ \t\r\n]+ -> skip ;