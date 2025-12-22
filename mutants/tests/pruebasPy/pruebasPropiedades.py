import pytest
from hypothesis import given, strategies as st, settings
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, BASE_DIR)

from src.python.busquedaBinaria import busqueda_binaria, busqueda_binaria_recursiva

@given(
    st.lists(st.integers(), min_size=0, max_size=100).map(sorted),
    st.integers(min_value=-1000, max_value=1000)
)
def test_propiedad_busqueda_binaria(lista_ordenada, objetivo):
    """
    Prueba basada en propiedades para búsqueda binaria.
    Verifica que el resultado sea correcto para cualquier lista ordenada y objetivo.
    """
    resultado = busqueda_binaria(lista_ordenada, objetivo)
    
    if objetivo in lista_ordenada:
        # Si el objetivo está en la lista, debe devolver un índice válido
        assert isinstance(resultado, int)
        assert 0 <= resultado < len(lista_ordenada)
        assert lista_ordenada[resultado] == objetivo
        
        # Verificar que todos los elementos antes del índice son menores
        for i in range(resultado):
            assert lista_ordenada[i] <= objetivo
            
        # Verificar que todos los elementos después del índice son mayores
        for i in range(resultado + 1, len(lista_ordenada)):
            assert lista_ordenada[i] >= objetivo
    else:
        # Si el objetivo no está en la lista, debe devolver -1
        assert resultado == -1

@given(
    st.lists(st.integers(), min_size=0, max_size=50).map(sorted),
    st.integers(min_value=-100, max_value=100)
)
def test_propiedad_busqueda_recursiva(lista_ordenada, objetivo):
    """
    Prueba basada en propiedades para la versión recursiva.
    """
    resultado_iterativo = busqueda_binaria(lista_ordenada, objetivo)
    resultado_recursivo = busqueda_binaria_recursiva(lista_ordenada, objetivo)
    assert resultado_iterativo == resultado_recursivo

@given(st.lists(st.integers(), min_size=1, max_size=20).map(sorted))
def test_propiedad_extremos_ordenados(lista):
    """
    Verifica propiedades de búsqueda en extremos de listas ordenadas.
    """
    # Primer elemento (puede devolver cualquier índice válido)
    res_inicio = busqueda_binaria(lista, lista[0])
    assert 0 <= res_inicio < len(lista)
    assert lista[res_inicio] == lista[0]

    # Último elemento (puede devolver cualquier índice válido)
    res_final = busqueda_binaria(lista, lista[-1])
    assert 0 <= res_final < len(lista)
    assert lista[res_final] == lista[-1]
    
    # Elemento no existente menor que el mínimo
    assert busqueda_binaria(lista, lista[0] - 1) == -1
    
    # Elemento no existente mayor que el máximo
    assert busqueda_binaria(lista, lista[-1] + 1) == -1

@given(st.lists(st.integers(), min_size=0, max_size=10))
def test_propiedad_lista_vacia_y_duplicados(lista):
    """
    Prueba con listas vacías y con duplicados.
    """
    if not lista:
        assert busqueda_binaria([], 5) == -1
    else:
        # Crear lista con duplicados ordenada
        lista_ordenada = sorted(lista + lista)
        for valor in set(lista_ordenada):
            resultado = busqueda_binaria(lista_ordenada, valor)
            assert resultado != -1
            assert lista_ordenada[resultado] == valor