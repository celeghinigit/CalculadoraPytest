import math
import Calculadora
from Calculadora import somar


def testSomar2Mais3():
    assert somar(2, 3) == 5


def testSomar4Mais6():
    assert somar(4, 6) == 10


def testDivisaoPorZero():
    assert math.isnan(Calculadora.dividir(10, 0))