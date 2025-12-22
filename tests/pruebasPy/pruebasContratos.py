import pytest
import icontract
import sys
import os
from typing import List

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, BASE_DIR)

from src.python.busquedaBinaria import busqueda_binaria

# Contrato para búsqueda binaria
@icontract.require(lambda arr: arr == sorted(arr))
@icontract.require(lambda arr: len(arr) <= 1000)
@icontract.ensure(
    lambda result, arr, objetivo: result == -1
    or (0 <= result < len(arr) and arr[result] == objetivo)
)
@icontract.ensure(
    lambda result, arr, objetivo: result == -1
    or all(arr[i] <= objetivo for i in range(result))
)
@icontract.ensure(
    lambda result, arr, objetivo: result == -1
    or all(arr[i] >= objetivo for i in range(result + 1, len(arr)))
)
def busqueda_binaria_con_contrato(arr: List[int], objetivo: int) -> int:
    return busqueda_binaria(arr, objetivo)

# Contrato adicional
@icontract.require(lambda x: x >= 0)
@icontract.ensure(lambda result, x: result >= 0)
def raiz_cuadrada_entera(x: int) -> int:
    if x == 0 or x == 1:
        return x

    bajo, alto = 1, x // 2
    while bajo <= alto:
        medio = (bajo + alto) // 2
        cuadrado = medio * medio

        if cuadrado == x:
            return medio
        elif cuadrado < x:
            bajo = medio + 1
        else:
            alto = medio - 1

    return alto

# Clase con invariantes 
@icontract.invariant(lambda self: self.valores == sorted(self.valores))
@icontract.invariant(lambda self: all(isinstance(x, int) for x in self.valores))
@icontract.invariant(lambda self: len(self.valores) <= 100)
class ContadorOrdenado:

    def __init__(self):
        self.valores: List[int] = []

    @icontract.require(lambda valor: isinstance(valor, int))
    def agregar(self, valor: int) -> None:
        for i, v in enumerate(self.valores):
            if v > valor:
                self.valores.insert(i, valor)
                return
        self.valores.append(valor)

    @icontract.require(lambda self, indice: 0 <= indice < len(self.valores))
    def eliminar(self, indice: int) -> None:
        del self.valores[indice]

# Tests
def test_busqueda_binaria_con_contrato_ok():
    lista = [1, 2, 2, 3, 4]
    assert busqueda_binaria_con_contrato(lista, 2) in [1, 2]


def test_busqueda_binaria_con_contrato_falla():
    with pytest.raises(Exception):
        busqueda_binaria_con_contrato([3, 1, 2], 1)


def test_raiz_cuadrada_entera():
    assert raiz_cuadrada_entera(9) == 3
    assert raiz_cuadrada_entera(8) == 2


def test_contador_ordenado():
    c = ContadorOrdenado()
    c.agregar(3)
    c.agregar(1)
    c.agregar(2)
    assert c.valores == [1, 2, 3]
    c.eliminar(1)
    assert c.valores == [1, 3]
