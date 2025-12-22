# flaky_detection.py - Script para detectar pruebas inestables

import subprocess
import sys
import os
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, BASE_DIR)

from src.python.busquedaBinaria import busqueda_binaria

def run_flakefinder():
    """
    Ejecuta pytest-flakefinder para detectar pruebas inconsistentes
    """
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/pruebasPy/",
        "--flakefinder",
        "--flakefinder-count=30",
        "-v",
        "--tb=short"
    ]

    print("Analizando inconsistencias en 30 ejecuciones por prueba \n")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Guardar resultados
    timestamp = datetime.now().strftime("%Y%m%d")
    report_file = f"flaky_report_{timestamp}.txt"
    
    with open(report_file, "w") as f:
        f.write(f" REPORTE - {timestamp} ")
        f.write(result.stdout)
        if result.stderr:
            f.write("  ERRORES ")
            f.write(result.stderr)
    
    print(f" Resultados guardados: {report_file}")
    return result.returncode == 0

def run_rerunfailures():
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/pruebasPy",
        "--reruns", "3",
        "--reruns-delay", "0.5",
        "-v",
        "--tb=short"
    ]
    print("Reintentando pruebas fallidas hasta 3 veces...")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Analizar salida para detectar reintentos
    output_lines = result.stdout.split('\n')  
    contador_reintentos = sum(1 for line in output_lines if 'RERUN' in line)  # 
    
    if contador_reintentos > 0:
        print(f"Se detectaron {contador_reintentos} reintentos posibles")
    else:
        print("No se detectaron reintentos necesarios")
    
    return result.returncode == 0

def run_parallel_detection():
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/pruebasPy", 
        "-n", "auto",
        "--random-order",
        "-v"
    ]
    print("Buscando problemas de concurrencia y orden...")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0

def main():
    print("INICIANDO ANÁLISIS DE PRUEBAS INESTABLES")
    
    # Flakefinder
    flakefinder_ok = run_flakefinder()
    
    # Rerunfailures
    rerun_ok = run_rerunfailures()
    
    # Detección paralela
    parallel_ok = run_parallel_detection()

# Ejecutar el programa
if __name__ == "__main__":
    main()
    
