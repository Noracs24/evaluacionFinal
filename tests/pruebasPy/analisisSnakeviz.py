"""
Genera un perfil de ejecución (cProfile) y opcionalmente lo abre con SnakeViz.

Uso:
  python3 tests/pruebasPy/analisisSnakeviz.py
  python3 tests/pruebasPy/analisisSnakeviz.py --output /tmp/perfil.prof
  python3 tests/pruebasPy/analisisSnakeviz.py --open

Nota: para visualizar con SnakeViz:
  pip install snakeviz
"""

from __future__ import annotations

import argparse
import cProfile
import importlib.util
import os
import subprocess
import sys
from pathlib import Path

# Permite ejecutar el script desde cualquier carpeta sin romper imports.
BASE_DIR = Path(__file__).resolve().parents[2]  # /workspace
sys.path.insert(0, str(BASE_DIR))

from src.python.busquedaBinaria import busqueda_binaria, busqueda_binaria_recursiva


def workload_equivalente_timeit(
    datos: list[int],
    objetivo: int,
    iteraciones_iterativa: int,
    iteraciones_recursiva: int,
) -> None:
    for _ in range(iteraciones_iterativa):
        busqueda_binaria(datos, objetivo)

    for _ in range(iteraciones_recursiva):
        busqueda_binaria_recursiva(datos, objetivo)


def snakeviz_instalado() -> bool:
    return importlib.util.find_spec("snakeviz") is not None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Genera un .prof para analizar con SnakeViz.")
    parser.add_argument(
        "--output",
        default=str(Path(__file__).parent / "perfil_busquedas.prof"),
        help="Ruta del archivo .prof de salida.",
    )
    parser.add_argument(
        "--iter-iterativa",
        type=int,
        default=1000,
        help="Iteraciones para la búsqueda binaria iterativa.",
    )
    parser.add_argument(
        "--iter-recursiva",
        type=int,
        default=1000,
        help="Iteraciones para la búsqueda binaria recursiva.",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="Abre el perfil con SnakeViz (si está instalado).",
    )
    args = parser.parse_args(argv)

    datos = list(range(10000))
    objetivo = datos[len(datos) // 2]

    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print("Generando perfil equivalente a timeit")
    profiler = cProfile.Profile()
    profiler.enable()
    workload_equivalente_timeit(
        datos=datos,
        objetivo=objetivo,
        iteraciones_iterativa=args.iter_iterativa,
        iteraciones_recursiva=args.iter_recursiva,
    )
    profiler.disable()
    profiler.dump_stats(str(output_path))

    print(f"Perfil generado correctamente: {output_path}")

    if not args.open:
        if snakeviz_instalado():
            print("Para visualizar: python3 -m snakeviz", str(output_path))
        else:
            print("Para visualizar: pip install snakeviz  # y luego: python3 -m snakeviz", str(output_path))
        return 0

    if not snakeviz_instalado():
        print("SnakeViz no está instalado. Instálalo con: pip install snakeviz")
        return 2

    # Esto abre un servidor/visor; puede bloquear hasta que se cierre.
    return subprocess.call([sys.executable, "-m", "snakeviz", str(output_path)])


if __name__ == "__main__":
    raise SystemExit(main())
