import subprocess
import re
import sys
import os
from typing import Dict

# -------------------------
# Ajuste de paths
# -------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, BASE_DIR)

from src.python.busquedaBinaria import busqueda_binaria


# -------------------------
# Ejecutar comandos shell
# -------------------------
def ejecutar_comando(comando: str) -> str:
    resultado = subprocess.run(
        comando,
        shell=True,
        capture_output=True,
        text=True
    )
    return resultado.stdout


# -------------------------
# Obtener cobertura
# -------------------------
def obtener_cobertura() -> Dict[str, float]:
    comando = "pytest tests/pruebasPy/ --cov=src/python --cov-report=term"
    salida = ejecutar_comando(comando)

    cobertura = {}

    # Formato real de pytest-cov
    patron = r"(src/python/[^\s]+\.py)\s+\d+\s+\d+\s+(\d+)%"

    for match in re.finditer(patron, salida):
        archivo = match.group(1)
        porcentaje = float(match.group(2))
        cobertura[archivo] = porcentaje

    print(f"\nCobertura obtenida: {cobertura}")
    return cobertura


# -------------------------
# Obtener mutación (ROBUSTO)
# -------------------------
def obtener_puntuacion_mutacion() -> Dict[str, float]:
    ejecutar_comando("rm -rf .mutmut-cache")

    ejecutar_comando("mutmut run --paths-to-mutate=src/python/")
    salida = ejecutar_comando("mutmut results")

    mutacion = {}

    archivo_actual = None
    total = 0
    killed = 0

    for linea in salida.splitlines():
        # Ejemplo: ---- src/python/busquedaBinaria.py (7) ----
        if linea.startswith("----") and ".py" in linea:
            if archivo_actual and total > 0:
                mutacion[archivo_actual] = (killed / total) * 100

            match = re.search(r"---- (.+?) \((\d+)\) ----", linea)
            if match:
                archivo_actual = match.group(1)
                total = int(match.group(2))
                killed = 0

        # Mutantes eliminados suelen marcarse con [x]
        elif "[x]" in linea:
            killed += 1

    if archivo_actual and total > 0:
        mutacion[archivo_actual] = (killed / total) * 100

    print(f"\nPuntuación de mutación obtenida: {mutacion}")
    return mutacion


# -------------------------
# Análisis cobertura vs defectos
# -------------------------
def analizar_relacion(cobertura: Dict[str, float], mutacion: Dict[str, float]) -> None:
    print(f"\n{'Archivo':<40} {'Cobertura':<12} {'Mutación':<12} {'Diferencia':<12} Calidad")
    print("-" * 90)

    for archivo, cov in cobertura.items():
        if archivo in mutacion:
            mut = mutacion[archivo]
            diff = cov - mut

            if diff <= 5:
                calidad = "Excelente"
            elif diff <= 15:
                calidad = "Buena"
            elif diff <= 25:
                calidad = "Regular"
            else:
                calidad = "Mejorar"

            print(f"{archivo:<40} {cov:>6.1f}%      {mut:>6.1f}%      {diff:>6.1f}%      {calidad}")

    if not cobertura or not mutacion:
        print("\nNo se pudieron obtener datos suficientes para el análisis")
        return

    cov_prom = sum(cobertura.values()) / len(cobertura)
    mut_prom = sum(mutacion.values()) / len(mutacion)
    brecha = cov_prom - mut_prom

    print("\nRESUMEN GLOBAL")
    print(f" Cobertura promedio: {cov_prom:.1f}%")
    print(f" Detección de defectos promedio: {mut_prom:.1f}%")
    print(f" Brecha promedio: {brecha:.1f}%")

    if brecha <= 10:
        print(" Calidad de pruebas: Alta")
    elif brecha <= 20:
        print(" Calidad de pruebas: Sólida")
    else:
        print(" Calidad de pruebas: Mejorable (alta cobertura ≠ alta detección)")


# -------------------------
# Main
# -------------------------
def main():
    print("\nANÁLISIS DE RELACIÓN COBERTURA VS DEFECTOS")

    if not os.path.exists("src/python/busquedaBinaria.py"):
        print("No se encuentra src/python/busquedaBinaria.py")
        return

    if not os.path.exists("tests/pruebasPy/"):
        print("No se encuentra tests/pruebasPy/")
        return

    cobertura = obtener_cobertura()
    mutacion = obtener_puntuacion_mutacion()
    analizar_relacion(cobertura, mutacion)


if __name__ == "__main__":
    main()
