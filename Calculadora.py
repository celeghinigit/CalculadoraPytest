def somar(a: int, b: int) -> int:
    return a + b


def dividir(a: float, b: float) -> float:
    if b == 0:
        return float('nan')
    return a / b