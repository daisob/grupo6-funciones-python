import math

def factorialcenturion(n):
    """Devuelve el factorial de un número entero no negativo."""
    if n < 0:
        return None
    return math.factorial(n)
