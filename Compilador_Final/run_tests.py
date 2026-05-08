#!/usr/bin/env python3
# ============================================================
#  run_tests.py — Automatización de pruebas DroneScript
#  Ejecuta todos los casos válidos e inválidos y reporta resultados
# ============================================================

import os
import sys
import subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
VALID_DIR   = os.path.join(ROOT, "tests", "valid")
INVALID_DIR = os.path.join(ROOT, "tests", "invalid")
MAIN        = os.path.join(ROOT, "main.py")

PASS = "✅ PASS"
FAIL = "❌ FAIL"


def run_test(drone_file: str, expect_success: bool) -> bool:
    """
    Ejecuta el compilador sobre un archivo .drone.
    Retorna True si el resultado coincide con la expectativa.
    """
    out_py  = drone_file.replace(".drone", "_out.py")
    out_log = drone_file.replace(".drone", "_log.txt")

    result = subprocess.run(
        [sys.executable, MAIN, drone_file, out_py, out_log],
        capture_output=True, text=True
    )

    compiled_ok = result.returncode == 0

    # Limpiar archivos temporales
    for f in (out_py, out_log):
        if os.path.exists(f):
            os.remove(f)

    return compiled_ok == expect_success


def collect(directory: str, ext=".drone"):
    files = sorted(
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.endswith(ext)
    )
    return files


def main():
    print("=" * 60)
    print("  DroneScript — Suite de Pruebas Automatizadas")
    print("=" * 60)

    valid_files   = collect(VALID_DIR)
    invalid_files = collect(INVALID_DIR)

    total = passed = 0

    # ── Pruebas válidas (se espera ÉXITO) ─────────────────────
    print(f"\n📂 PRUEBAS VÁLIDAS ({len(valid_files)} archivos)")
    print("-" * 60)
    for f in valid_files:
        ok = run_test(f, expect_success=True)
        status = PASS if ok else FAIL
        name = os.path.basename(f)
        print(f"  {status}  {name}")
        total += 1
        if ok:
            passed += 1

    # ── Pruebas con error (se espera FALLO) ───────────────────
    print(f"\n📂 PRUEBAS CON ERRORES ({len(invalid_files)} archivos)")
    print("-" * 60)
    for f in invalid_files:
        ok = run_test(f, expect_success=False)
        status = PASS if ok else FAIL
        name = os.path.basename(f)
        print(f"  {status}  {name}")
        total += 1
        if ok:
            passed += 1

    # ── Resumen ───────────────────────────────────────────────
    print("\n" + "=" * 60)
    print(f"  RESULTADO: {passed}/{total} pruebas pasaron")
    pct = (passed / total * 100) if total else 0
    print(f"  PORCENTAJE: {pct:.1f}%")
    if passed == total:
        print("  🎉 ¡Todas las pruebas pasaron!")
    else:
        print(f"  ⚠️  {total - passed} prueba(s) fallaron.")
    print("=" * 60)
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
