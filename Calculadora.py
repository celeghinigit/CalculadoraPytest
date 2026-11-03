def somar(a: int, b: int) -> int:
    return a+b

def subtrair(a: int, b: int) -> int:
    return a-b

def multiplicar(a: int, b: int) -> int:
    return a*b

def dividir(a: int, b: int) -> int:
    if b/0:
        return a/b
    else:
        return 0
