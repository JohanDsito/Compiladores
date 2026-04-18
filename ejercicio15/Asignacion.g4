grammar Asignacion;

stat: ID IGUAL NUM ;

IGUAL: '=';
ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;