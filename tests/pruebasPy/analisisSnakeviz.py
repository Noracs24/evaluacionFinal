import cProfile
import sys
import os
from pathlib import Path

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, BASE_DIR)

from src.python.busquedaBinaria import busqueda_binaria, busqueda_binaria_recursiva

datos = list(range(10000))
objetivo = 5000

def ejecutar_busquedas():
    for _ in range(1000):
        busqueda_binaria(datos, objetivo)
        busqueda_binaria_recursiva(datos, objetivo)

def main():
    print("Generando perfil de ejecución")
    carpeta_actual = Path(__file__).parent
    archivo = carpeta_actual / "perfil_busquedas.prof"

    profiler = cProfile.Profile()
    profiler.enable()
    ejecutar_busquedas()
    profiler.disable()
    profiler.dump_stats(archivo)

    print(f"Perfil generado correctamente: {archivo}")
    print("Ejecuta: snakeviz tests/pruebasPy/perfil_busquedas.prof")

if __name__ == "__main__":
    main()
