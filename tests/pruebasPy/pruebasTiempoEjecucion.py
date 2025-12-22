import timeit
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, BASE_DIR)

from src.python.busquedaBinaria import busqueda_binaria, busqueda_binaria_recursiva

def prueba_timeit_rapida():
    print("PRUEBA  DE RENDIMIENTO")
    
    tamaño = 10000
    datos = list(range(tamaño))
    objetivo = datos[tamaño // 2]  # Elemento del medio
    
    print(f"Datos: {tamaño:,} elementos")
    print(f" Objetivo: {objetivo} (posición {tamaño // 2})")
    
    # Configurar timeit
    number = 1000  # Número de ejecuciones por medición
    repeat = 5     # Número de mediciones repetidas
    
    # Prueba búsqueda binaria iterativa
    print(" Búsqueda Binaria Iterativa:")
    tiempo_iterativo = min(timeit.repeat(
        lambda: busqueda_binaria(datos, objetivo), 
        number=number, 
        repeat=repeat
    ))
    
    print(f" Tiempo mejor de {repeat} mediciones: {tiempo_iterativo:.6f}s")
    print(f" Tiempo promedio por llamada: {(tiempo_iterativo/number)*1e6:.2f} μs")
    
    # Prueba búsqueda binaria recursiva
    print("Búsqueda Binaria Recursiva:")
    tiempo_recursivo = min(timeit.repeat(
        lambda: busqueda_binaria_recursiva(datos, objetivo), 
        number=number, 
        repeat=repeat
    ))
    
    print(f" Tiempo mejor de {repeat} mediciones: {tiempo_recursivo:.6f}s")
    print(f" Tiempo promedio por llamada: {(tiempo_recursivo/number)*1e6:.2f} μs")

    # Comparación
    print(" COMPARACIÓN DE RENDIMIENTO:")
    if tiempo_iterativo < tiempo_recursivo:
        diferencia = ((tiempo_recursivo - tiempo_iterativo) / tiempo_iterativo) * 100
        print(f"  Iterativa es {diferencia:.1f}% más rápida")
        print(f"  Método recomendado: Iterativo")
    else:
        diferencia = ((tiempo_iterativo - tiempo_recursivo) / tiempo_recursivo) * 100
        print(f"  Recursiva es {diferencia:.1f}% más rápida")
        print(f"  Método recomendado: Recursivo")

def prueba_escalabilidad_rapida():
    print("\n PRUEBA DE ESCALABILIDAD RÁPIDA")
    print("=" * 40)
    
    tamaños = [1000, 2000, 4000, 8000]
    resultados = {}
    
    for tamaño in tamaños:
        datos = list(range(tamaño))
        objetivo = datos[tamaño // 2]
        
        # Medir tiempo (una sola medición rápida)
        tiempo = timeit.timeit(
            lambda: busqueda_binaria(datos, objetivo), 
            number=100
        )
        
        resultados[tamaño] = tiempo
        print(f"   {tamaño:4d} elementos: {tiempo:.6f}s")

if __name__ == "__main__":
    prueba_timeit_rapida()
    prueba_escalabilidad_rapida()