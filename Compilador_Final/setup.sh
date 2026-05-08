#!/usr/bin/env bash
# ============================================================
#  setup.sh — Configuración del entorno en GitHub Codespace
#  Genera los archivos ANTLR4 y verifica dependencias
# ============================================================

set -e

echo "=================================================="
echo "  DroneScript — Setup del entorno ANTLR4"
echo "=================================================="

# ── 1. Verificar Python ───────────────────────────────────
echo ""
echo "▶ Verificando Python..."
python3 --version || { echo "❌ Python3 no encontrado"; exit 1; }

# ── 2. Instalar antlr4-python3-runtime ────────────────────
echo ""
echo "▶ Instalando antlr4-python3-runtime..."
pip install antlr4-python3-runtime==4.13.1 --quiet
echo "  ✅ antlr4-python3-runtime instalado"

# ── 3. Verificar que existe el JAR de ANTLR4 ─────────────
ANTLR_JAR=""
for candidate in \
    "/usr/local/lib/antlr4.jar" \
    "/usr/local/lib/antlr-4.13.1-complete.jar" \
    "$HOME/antlr4.jar" \
    "antlr4.jar" \
    "antlr-4.13.1-complete.jar"
do
    if [ -f "$candidate" ]; then
        ANTLR_JAR="$candidate"
        break
    fi
done

if [ -z "$ANTLR_JAR" ]; then
    echo ""
    echo "▶ Descargando ANTLR4 JAR..."
    wget -q https://www.antlr.org/download/antlr-4.13.1-complete.jar -O antlr4.jar
    ANTLR_JAR="antlr4.jar"
    echo "  ✅ antlr4.jar descargado"
fi

echo "  ✅ ANTLR4 JAR: $ANTLR_JAR"

# ── 4. Verificar Java ────────────────────────────────────
echo ""
echo "▶ Verificando Java..."
java -version 2>&1 | head -1 || { echo "❌ Java no encontrado. Instalar con: sudo apt install default-jre"; exit 1; }

# ── 5. Generar archivos Python desde la gramática ─────────
echo ""
echo "▶ Generando Lexer/Parser/Visitor desde gramatica.g4..."
mkdir -p generated

java -jar "$ANTLR_JAR" \
    -Dlanguage=Python3 \
    -visitor \
    -o generated \
    gramatica.g4

# Mover archivos si quedaron en subdirectorio
if [ -d "generated/." ]; then
    # ANTLR a veces crea subcarpeta con el nombre del paquete
    find generated -name "*.py" -not -path "generated/*.py" \
        -exec mv {} generated/ \; 2>/dev/null || true
    find generated -name "*.tokens" -delete 2>/dev/null || true
    find generated -name "*.interp" -delete 2>/dev/null || true
fi

# Crear __init__.py si no existe
touch generated/__init__.py

echo "  ✅ Archivos generados:"
ls generated/*.py 2>/dev/null | sed 's/^/     /'

# ── 6. Prueba rápida de compilación ──────────────────────
echo ""
echo "▶ Prueba rápida con input.txt..."
python3 main.py input.txt output_program.py output.txt && echo "  ✅ Compilación de prueba exitosa" || echo "  ⚠️  Revisar errores arriba"

echo ""
echo "=================================================="
echo "  ✅ Setup completo. Para compilar usa:"
echo "     python3 main.py input.txt"
echo ""
echo "  Para correr todas las pruebas:"
echo "     python3 run_tests.py"
echo "=================================================="
