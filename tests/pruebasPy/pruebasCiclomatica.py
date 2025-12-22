# Código para analizar complejidad ciclomática
from radon.complexity import cc_visit, cc_rank
import ast

def analizar_complejidad_por_funcion(codigo_fuente):
    try:
        # Analizar el código fuente con Radon
        resultados = cc_visit(codigo_fuente)
        
        analisis = {}
        for bloque in resultados:
            if hasattr(bloque, 'name') and hasattr(bloque, 'complexity'):
                nombre_funcion = bloque.name
                complejidad = bloque.complexity
                ranking = cc_rank(complejidad)
                linea = getattr(bloque, 'lineno', 'N/A')
                
                analisis[nombre_funcion] = {
                    'complejidad': complejidad,
                    'ranking': ranking,
                    'linea': linea,
                    'evaluacion': evaluar_complejidad(complejidad)
                }
        
        return analisis
    except Exception as e:
        return {'error': str(e)}

def evaluar_complejidad(complejidad):
    if complejidad <= 5:
        return "Código simple y mantenible"
    elif complejidad <= 10:
        return "Código moderadamente complejo"
    elif complejidad <= 15:
        return "Código algo complejo, considerar refactorización"
    elif complejidad <= 20:
        return "Código complejo, necesita refactorización"
    else:
        return "Código muy complejo, refactorización urgente"

# Ejemplo de uso
if __name__ == "__main__":
    # Leer el archivo de búsqueda binaria
    with open('src/python/busquedaBinaria.py', 'r') as f:
        codigo = f.read()
    
    resultados = analizar_complejidad_por_funcion(codigo)
    
    print("ANÁLISIS DE COMPLEJIDAD CICLOMÁTICA ")
    for func, datos in resultados.items():
        print(f"\nFunción: {func}")
        print(f"  Línea: {datos['linea']}")
        print(f"  Complejidad: {datos['complejidad']} ({datos['ranking']})")
        print(f"  Evaluación: {datos['evaluacion']}")