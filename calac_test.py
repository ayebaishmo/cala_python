from .calac import Calc
import pytest

@pytest.fixture
def Calc_20():
    return Calc(20)


def test_addition(Calc_20):
    assert Calc_20.addition(6, 7) == 13

def test_subtract(Calc_20):
    assert Calc_20.subtract(5, 10) == -5

def test_mult(Calc_20):
    assert Calc_20.multiplication(4, 5) == 20
    