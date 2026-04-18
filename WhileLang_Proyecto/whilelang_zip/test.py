"""
test.py — Ejecuta los 10 casos de prueba de la practica de WhileLang.

Uso:
    python test.py

Requisito: los archivos generados por ANTLR deben estar en la carpeta 'generated/'.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))

from antlr4 import CommonTokenStream, InputStream
from generated.WhileLangLexer import WhileLangLexer
from generated.WhileLangParser import WhileLangParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor


def run_test(number: int, description: str, code: str):
    """Ejecuta un caso de prueba e imprime la salida."""
    separator = "=" * 60
    print(f"\n{separator}")
    print(f"Caso {number}: {description}")
    print(f"{separator}")
    print("Codigo de entrada:")
    print(code.strip())
    print("\nSalida obtenida:")

    input_stream = InputStream(code)
    lexer = WhileLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = WhileLangParser(token_stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"[ERROR SINTACTICO] {parser.getNumberOfSyntaxErrors()} error(es) de sintaxis.")
        return

    visitor = SemanticVisitor()
    visitor.visit(tree)

    if not visitor.errors:
        print("Sin errores semanticos. Programa valido.")


# ---------------------------------------------------------------------------
# Casos de prueba
# ---------------------------------------------------------------------------

TESTS = [
    (
        1,
        "Declaraciones y asignaciones validas (int y string)",
        """
int x = 10;
string s = "hola";
x = x + 5;
s = s + " mundo";
"""
    ),
    (
        2,
        "Error: asignacion de tipo incorrecto",
        """
int x = 10;
string s = "hola";
x = s;
"""
    ),
    (
        3,
        "Error: variable no declarada",
        """
y = 5;
"""
    ),
    (
        4,
        "Error: redeclaracion en el mismo ambito",
        """
int x = 1;
string x = "hola";
"""
    ),
    (
        5,
        "Error: condicion incorrecta en if (string como condicion)",
        """
string s = "hola";
if (s) {
  int x = 0;
}
"""
    ),
    (
        6,
        "While con strings — comparacion invalida",
        """
string a = "hola";
string b = "mundo";
while (a < b) {
  break;
}
"""
    ),
    (
        7,
        "If con else y scopes independientes",
        """
int x = 0;
if (x < 5) {
  int y = 10;
} else {
  int y = 20;
}
"""
    ),
    (
        8,
        "Anidamiento de while + if con scopes anidados",
        """
int i = 0;
while (i < 3) {
  int j = 0;
  while (j < 2) {
    if (i == j) {
      j = j + 1;
    }
    j = j + 1;
  }
  i = i + 1;
}
"""
    ),
    (
        9,
        "Uso de continue y break en while",
        """
int i = 0;
while (i < 5) {
  if (i == 2) {
    continue;
  }
  if (i == 4) {
    break;
  }
  i = i + 1;
}
"""
    ),
    (
        10,
        "Error: operacion aritmetica entre strings",
        """
string s = "hola";
string t = "mundo";
string u = s * t;
"""
    ),
]


def main():
    print("╔══════════════════════════════════════════════════════════╗")
    print("║    SUITE DE PRUEBAS — Analisis Semantico WhileLang       ║")
    print("╚══════════════════════════════════════════════════════════╝")

    for number, description, code in TESTS:
        run_test(number, description, code)

    print("\n" + "=" * 60)
    print("Suite de pruebas completada.")
    print("=" * 60)


if __name__ == '__main__':
    main()
