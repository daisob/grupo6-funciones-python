from funciones.factorialcenturion import factorialcenturion

def test_factorialcenturion():
    assert factorialcenturion(5) == 120
    assert factorialcenturion(0) == 1
    assert factorialcenturion(-3) is None
