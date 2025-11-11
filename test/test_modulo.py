# tests/test_modulo.py
from funciones.modulo import modulo

def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(7, 7) == 0
    assert modulo(5, 2) == 1
    assert modulo(8, 0) is None
