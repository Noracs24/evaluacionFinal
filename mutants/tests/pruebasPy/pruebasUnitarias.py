import pytest
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, BASE_DIR)

from src.python.busquedaBinaria import busqueda_binaria, busqueda_binaria_recursiva

class TestBusquedaBinaria:
    """Suite de pruebas unitarias para búsqueda binaria."""
    
    def test_lista_vacia(self):
        """Prueba con lista vacía."""
        assert busqueda_binaria([], 5) == -1
        assert busqueda_binaria_recursiva([], 5) == -1
    
    def test_elemento_unico(self):
        """Prueba con lista de un elemento."""
        assert busqueda_binaria([5], 5) == 0
        assert busqueda_binaria([5], 3) == -1
        assert busqueda_binaria_recursiva([5], 5) == 0
        assert busqueda_binaria_recursiva([5], 3) == -1
    
    def test_elementos_multiples(self):
        """Prueba con múltiples elementos."""
        lista = [1, 3, 5, 7, 9, 11, 13]
        
        # Primer elemento
        assert busqueda_binaria(lista, 1) == 0
        assert busqueda_binaria_recursiva(lista, 1) == 0
        
        # Elementos intermedios
        assert busqueda_binaria(lista, 5) == 2
        assert busqueda_binaria_recursiva(lista, 5) == 2
        assert busqueda_binaria(lista, 9) == 4
        assert busqueda_binaria_recursiva(lista, 9) == 4
        
        # Último elemento
        assert busqueda_binaria(lista, 13) == 6
        assert busqueda_binaria_recursiva(lista, 13) == 6
        
        # Elementos no existentes
        assert busqueda_binaria(lista, 0) == -1
        assert busqueda_binaria(lista, 2) == -1
        assert busqueda_binaria(lista, 14) == -1
        assert busqueda_binaria_recursiva(lista, 0) == -1
        assert busqueda_binaria_recursiva(lista, 2) == -1
        assert busqueda_binaria_recursiva(lista, 14) == -1
    
    def test_numeros_negativos(self):
        """Prueba con números negativos."""
        lista = [-10, -5, 0, 5, 10]
        assert busqueda_binaria(lista, -10) == 0
        assert busqueda_binaria(lista, -5) == 1
        assert busqueda_binaria(lista, 0) == 2
        assert busqueda_binaria(lista, 5) == 3
        assert busqueda_binaria(lista, 10) == 4
        assert busqueda_binaria(lista, -3) == -1
    
    def test_lista_con_duplicados(self):
        """Prueba con lista que contiene duplicados."""
        lista = [1, 2, 2, 2, 3, 4, 4, 5]
        resultado = busqueda_binaria(lista, 2)
        assert resultado in [1, 2, 3]  # Cualquier índice donde esté el 2
        assert lista[resultado] == 2
        
        resultado = busqueda_binaria(lista, 4)
        assert resultado in [5, 6]
        assert lista[resultado] == 4
    
    def test_lista_grande(self):
        """Prueba con lista grande."""
        lista = list(range(0, 1000, 2))  # [0, 2, 4, ..., 998]
        
        # Buscar elementos que existen
        assert busqueda_binaria(lista, 0) == 0
        assert busqueda_binaria(lista, 500) == 250
        assert busqueda_binaria(lista, 998) == 499
        
        # Buscar elementos que no existen
        assert busqueda_binaria(lista, 1) == -1
        assert busqueda_binaria(lista, 999) == -1
    
    def test_tipos_de_datos(self):
        """Prueba con diferentes tipos de datos."""
        # Con floats convertidos a int
        lista = [1.0, 2.5, 3.7]
        assert busqueda_binaria([int(x) for x in lista], 2) == 1
        
        # Con strings (orden alfabético)
        lista_strings = ["apple", "banana", "cherry", "date"]
        # Nota: La implementación actual solo funciona con int
        # Esto mostraría TypeError, lo cual es comportamiento esperado
    
    def test_entradas_invalidas(self):
        """Prueba con entradas inválidas."""
        lista = [1, 2, 3]
        
        # Lista None
        with pytest.raises(TypeError):
            busqueda_binaria(None, 2)
        
        # Objetivo None
        with pytest.raises(TypeError):
            busqueda_binaria(lista, None)
        
        # Lista con elementos no comparables
        with pytest.raises(TypeError):
            busqueda_binaria([1, "dos", 3], 2)