import pytest


from .math_utils import MathUtils


math_utils = MathUtils()

def test_add_pos():
    assert math_utils.add(3, 8) == 11

def test_add_neg():
    assert math_utils.add(-20, -50) == -70

def test_divide_n():
    assert math_utils.divide(0, 3) == 3

def test_divide_z():
    with pytest.raises(ZeroDivisionError):
        math_utils.divide(3, 0)


def test_is_even():
    assert math_utils.is_even(8)

def test_is_even():
    assert math_utils.is_even(0)