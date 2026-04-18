"""
main.py — Punto de entrada principal para el analizador semantico de WhileLang.

Uso:
    python main.py <archivo.txt>

Ejemplo:
    python main.py input.txt
"""

import sys
import os

# Agregar la carpeta 'generated' al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))

from antlr4 import CommonTokenStream, FileStream, InputStream
from generated.WhileLangLexer import WhileLangLexer
from generated.WhileLangParser import WhileLangParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor


def analyze(source: str, from_file: bool = False):
    """
    Ejecuta el analisis lexico, sintactico y semantico sobre el codigo fuente.

    Args:
        source:    Ruta al archivo o cadena de codigo fuente.
        from_file: True si source es una ruta de archivo.
    """
    if from_file:
        input_stream = FileStream(source, encoding='utf-8')
    else:
        input_stream = InputStream(source)

    # --- Lexer ---
    lexer = WhileLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # --- Parser ---
    parser = WhileLangParser(token_stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"[ERROR SINTACTICO] Se encontraron {parser.getNumberOfSyntaxErrors()} error(es) de sintaxis.")
        return False

    # --- Analisis semantico ---
    visitor = SemanticVisitor()
    visitor.visit(tree)

    if visitor.errors:
        print(f"\n[Analisis completo] Se encontraron {len(visitor.errors)} error(es) semantico(s).")
        return False
    else:
        print("[Analisis completo] Sin errores semanticos. Programa valido.")
        return True


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo.txt>")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"Error: el archivo '{filepath}' no existe.")
        sys.exit(1)

    print(f"=== Analizando: {filepath} ===\n")
    analyze(filepath, from_file=True)


if __name__ == '__main__':
    main()
