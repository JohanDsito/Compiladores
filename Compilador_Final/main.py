#!/usr/bin/env python3
# ============================================================
#  main.py — Punto de integración del Mini-Compilador DroneScript
#  Ejecuta todas las fases: Léxico → Sintáctico → Semántico → Codegen
# ============================================================

import sys
import os
import subprocess

# Asegurar que los módulos generados por ANTLR4 estén en el path
sys.path.insert(0, os.path.dirname(__file__))

from antlr4 import CommonTokenStream, FileStream, InputStream
from antlr4.error.ErrorListener import ErrorListener

from generated.gramaticaLexer  import gramaticaLexer
from generated.gramaticaParser import gramaticaParser
from semantic_analyzer         import SemanticAnalyzer
from codegen                   import CodeGenerator


# ─── LISTENER DE ERRORES PERSONALIZADO ──────────────────────

class DroneErrorListener(ErrorListener):
    """Captura errores léxicos y sintácticos con mensajes claros."""

    def __init__(self, phase_name):
        super().__init__()
        self.errors = []
        self.phase_name = phase_name

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = (
            f"[Error {self.phase_name} - Línea {line}, Col {column}] "
            f"Token inesperado: '{offendingSymbol}' — {msg}"
        )
        self.errors.append(error_msg)
        print(f"  ❌ {error_msg}")


# ─── FUNCIONES DE FASE ───────────────────────────────────────

def phase_lexer(source_text: str):
    """
    FASE 1 — Análisis Léxico
    Convierte el texto fuente en una secuencia de tokens.
    """
    print("\n┌─────────────────────────────────────────────┐")
    print("│       FASE 1: ANÁLISIS LÉXICO                │")
    print("└─────────────────────────────────────────────┘")

    input_stream = InputStream(source_text)
    lexer = gramaticaLexer(input_stream)

    error_listener = DroneErrorListener("Léxico")
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    tokens = token_stream.tokens
    symbolic = lexer.symbolicNames

    print(f"  Total de tokens: {len(tokens) - 1}")  # -1 por EOF
    print(f"  {'TOKEN':<20} {'TIPO':<20} {'LÍNEA'}")
    print(f"  {'-'*55}")
    for tok in tokens:
        if tok.type == -1:   # EOF
            continue
        type_name = symbolic[tok.type] if tok.type < len(symbolic) else str(tok.type)
        print(f"  {tok.text:<20} {type_name:<20} {tok.line}")

    if error_listener.errors:
        return None, error_listener.errors

    # Reiniciar stream para el parser
    input_stream2 = InputStream(source_text)
    lexer2 = gramaticaLexer(input_stream2)
    lexer2.removeErrorListeners()
    lexer2.addErrorListener(error_listener)
    token_stream2 = CommonTokenStream(lexer2)

    print("\n  ✅ Análisis léxico completado sin errores.")
    return token_stream2, []


def phase_parser(token_stream):
    """
    FASE 2 — Análisis Sintáctico
    Construye el AST a partir del flujo de tokens.
    """
    print("\n┌─────────────────────────────────────────────┐")
    print("│       FASE 2: ANÁLISIS SINTÁCTICO            │")
    print("└─────────────────────────────────────────────┘")

    parser = gramaticaParser(token_stream)

    error_listener = DroneErrorListener("Sintáctico")
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if error_listener.errors:
        return None, error_listener.errors

    print("  Árbol de derivación (LISP):")
    print(f"  {tree.toStringTree(recog=parser)}")
    print("\n  ✅ Análisis sintáctico completado sin errores.")
    return tree, []


def phase_semantic(tree):
    """
    FASE 3 — Análisis Semántico
    Valida reglas de contexto, tabla de símbolos y tipos.
    """
    analyzer = SemanticAnalyzer()
    ok = analyzer.analyze(tree)
    return analyzer, ok


def phase_codegen(tree, symbol_table, output_path: str):
    """
    FASE 4 — Generación de Código Intermedio y traducción a Python.
    """
    generator = CodeGenerator(symbol_table)
    python_code = generator.generate(tree)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(python_code)

    print(f"\n  ✅ Código Python generado en: {output_path}")
    return python_code


# ─── COMPILADOR COMPLETO ─────────────────────────────────────

def compile_drone(input_file: str, output_file: str = "output_program.py",
                  log_file: str = "output.txt"):
    """
    Ejecuta el pipeline completo del compilador DroneScript.
    """
    separator = "=" * 55

    print(separator)
    print("   DroneScript Compiler — Mini-Compilador ANTLR4")
    print("   Universidad Cooperativa de Colombia")
    print(separator)
    print(f"   Archivo fuente : {input_file}")
    print(f"   Archivo salida : {output_file}")
    print(separator)

    # Leer fuente
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            source_text = f.read()
    except FileNotFoundError:
        print(f"\n❌ Archivo no encontrado: {input_file}")
        sys.exit(1)

    logs = []

    # ── Fase 1: Léxico ─────────────────────────────────────
    token_stream, lex_errors = phase_lexer(source_text)
    if lex_errors:
        print(f"\n❌ Compilación abortada: errores léxicos.")
        _write_log(log_file, source_text, lex_errors, [], [], "LÉXICO")
        return False

    # ── Fase 2: Sintáctico ─────────────────────────────────
    tree, syn_errors = phase_parser(token_stream)
    if syn_errors:
        print(f"\n❌ Compilación abortada: errores sintácticos.")
        _write_log(log_file, source_text, [], syn_errors, [], "SINTÁCTICO")
        return False

    # ── Fase 3: Semántico ──────────────────────────────────
    analyzer, sem_ok = phase_semantic(tree)
    if not sem_ok:
        sem_errors = [str(e) for e in analyzer.errors]
        print(f"\n❌ Compilación abortada: errores semánticos.")
        _write_log(log_file, source_text, [], [], sem_errors, "SEMÁNTICO")
        return False

    # ── Fase 4: Generación de código ──────────────────────
    python_code = phase_codegen(tree, analyzer.symbol_table, output_file)

    # ── Verificación: ejecutar el Python generado ──────────
    print("\n┌─────────────────────────────────────────────┐")
    print("│  FASE 5: VERIFICACIÓN DEL CÓDIGO GENERADO    │")
    print("└─────────────────────────────────────────────┘")
    result = subprocess.run(
        [sys.executable, output_file],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode == 0:
        print(f"  ✅ Script Python ejecutado correctamente.")
        if result.stdout:
            print(f"  Output: {result.stdout.strip()}")
    else:
        print(f"  ⚠️  El script generado tiene errores en ejecución:")
        print(f"  {result.stderr.strip()}")

    _write_log(log_file, source_text, [], [], [], "OK",
               python_code=python_code,
               warnings=[str(w) for w in analyzer.warnings],
               exec_output=result.stdout + result.stderr)

    print(f"\n{separator}")
    print("   ✅ COMPILACIÓN EXITOSA")
    print(f"{separator}\n")
    return True


def _write_log(log_file, source, lex_err, syn_err, sem_err,
               phase_failed, python_code="", warnings=None, exec_output=""):
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("DroneScript Compiler — Log de Ejecución\n")
        f.write("=" * 55 + "\n\n")
        f.write("── CÓDIGO FUENTE ──────────────────────────────\n")
        f.write(source + "\n\n")
        if lex_err:
            f.write("── ERRORES LÉXICOS ─────────────────────────────\n")
            for e in lex_err:
                f.write(f"  {e}\n")
        if syn_err:
            f.write("── ERRORES SINTÁCTICOS ──────────────────────────\n")
            for e in syn_err:
                f.write(f"  {e}\n")
        if sem_err:
            f.write("── ERRORES SEMÁNTICOS ───────────────────────────\n")
            for e in sem_err:
                f.write(f"  {e}\n")
        if warnings:
            f.write("── ADVERTENCIAS ─────────────────────────────────\n")
            for w in warnings:
                f.write(f"  {w}\n")
        if python_code:
            f.write("\n── CÓDIGO PYTHON GENERADO ───────────────────────\n")
            f.write(python_code + "\n")
        if exec_output:
            f.write("\n── OUTPUT DE EJECUCIÓN ──────────────────────────\n")
            f.write(exec_output + "\n")
        f.write("\n── RESULTADO ────────────────────────────────────\n")
        if phase_failed == "OK":
            f.write("COMPILACIÓN EXITOSA\n")
        else:
            f.write(f"COMPILACIÓN FALLIDA en fase: {phase_failed}\n")


# ─── PUNTO DE ENTRADA ────────────────────────────────────────

if __name__ == "__main__":
    input_file  = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output_program.py"
    log_file    = sys.argv[3] if len(sys.argv) > 3 else "output.txt"

    success = compile_drone(input_file, output_file, log_file)
    sys.exit(0 if success else 1)
