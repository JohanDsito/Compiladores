// ============================================================
//  DroneScript — Gramática ANTLR4
//  Mini-compilador para control de drones
//  Materia: Compiladores — Universidad Cooperativa de Colombia
// ============================================================

grammar gramatica;

// ─── REGLA INICIAL ──────────────────────────────────────────
program
    : (declaration | mission | command)+ EOF
    ;

// ─── DECLARACIONES ──────────────────────────────────────────
declaration
    : 'drone' ID ';'                                # DronDecl
    | 'zona' ID '(' NUMBER ',' NUMBER ')' ';'       # ZonaDecl
    ;

// ─── MISIONES ───────────────────────────────────────────────
mission
    : 'mision' ID '{' command+ '}'
    ;

// ─── COMANDOS ───────────────────────────────────────────────
command
    : action
    | control
    | waitCmd
    ;

// ─── ACCIONES ───────────────────────────────────────────────
action
    : ('despegar' | 'aterrizar' | 'hover') ID ';'          # SimpleAction
    | 'mover' ID direction NUMBER ';'                       # MoverAction
    | 'ir_a' ID ID ';'                                      # IrAAction
    | 'girar' ID ('izquierda' | 'derecha') NUMBER ';'       # GirarAction
    ;

// ─── DIRECCIÓN ──────────────────────────────────────────────
direction
    : 'adelante'
    | 'atras'
    | 'arriba'
    | 'abajo'
    | 'izquierda'
    | 'derecha'
    ;

// ─── ESTRUCTURAS DE CONTROL ─────────────────────────────────
control
    : 'si' condition ':' command ('sino' ':' command)?          # SiControl
    | 'repetir' NUMBER 'veces' '{' command+ '}'                 # RepetirControl
    ;

// ─── CONDICIÓN ──────────────────────────────────────────────
condition
    : ID '.' sensor comparator NUMBER
    ;

// ─── SENSORES ───────────────────────────────────────────────
sensor
    : 'altitud'
    | 'bateria'
    | 'distancia'
    ;

// ─── COMPARADORES ───────────────────────────────────────────
comparator
    : '<'
    | '>'
    | '=='
    | '<='
    | '>='
    ;

// ─── ESPERAR ────────────────────────────────────────────────
waitCmd
    : 'esperar' NUMBER 's' ';'
    ;

// ============================================================
//  REGLAS LÉXICAS
// ============================================================

// Identificadores: letras, dígitos, guión bajo
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;

// Números enteros y decimales positivos
NUMBER  : [0-9]+ ('.' [0-9]+)? ;

// Comentarios de línea estilo //
COMMENT : '//' ~[\r\n]* -> skip ;

// Comentarios de bloque estilo /* */
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;

// Espacios en blanco ignorados
WS      : [ \t\r\n]+ -> skip ;
