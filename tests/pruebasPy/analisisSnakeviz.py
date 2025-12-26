import cProfile
import sys
import os
from pathlib import Path

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, BASE_DIR)

from src.python.busquedaBinaria import (
    busqueda_binaria,
    busqueda_binaria_recursiva
)

datos = list(range(10000))
objetivo = datos[len(datos) // 2]

ITERACIONES_ITERATIVA = 1000
ITERACIONES_RECURSIVA = 1000


def workload_equivalente_timeit():
    for _ in range(ITERACIONES_ITERATIVA):
        busqueda_binaria(datos, objetivo)

    for _ in range(ITERACIONES_RECURSIVA):
        busqueda_binaria_recursiva(datos, objetivo)


def main():
    print("Generando perfil equivalente a timeit")

    carpeta = Path(__file__).parent
    archivo = carpeta / "perfil_busquedas.prof"

    profiler = cProfile.Profile()
    profiler.enable()

    workload_equivalente_timeit()

    profiler.disable()
    profiler.dump_stats(archivo)

    print(f"Perfil generado correctamente: {archivo}")
    print("Ábrelo con SnakeViz (doble clic o VS Code)")


if __name__ == "__main__":
    main()
