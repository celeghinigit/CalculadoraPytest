import math
from Calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(7, 3) == 4

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir():
    assert dividir(10, 2) == 5

def test_divisao_por_zero():
    assert math.isnan(dividir(10, 0))