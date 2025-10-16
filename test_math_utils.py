import pytest


from .math_utils import MathUtils


math_utils = MathUtils()


@pytest.fixture
def numbers():
    return {"test_add_pos":(3, 8), 
            "test_add_neg":(-20, -50), 
            "test_divide_n":(0, 3), 
            "test_divide_z":(3, 0), 
            "test_is_even_1": (8), 
            "test_is_even_2": (3), 
            "test_is_even_3": (0)
            }


def test_add_pos(numbers):
    a , b = numbers["test_add_pos"]
    assert math_utils.add(*numbers["test_add_pos"]) == 11

def test_add_neg():
    assert math_utils.add(-20, -50) == -70

def test_divide_n():
    assert math_utils.divide(0, 3) == 0

def test_divide_z():
    with pytest.raises(ZeroDivisionError):
        math_utils.divide(3, 0)


def test_is_even_1():
    assert math_utils.is_even(8)

def test_is_even_2():
    assert math_utils.is_even(3)

def test_is_even_3():
    assert math_utils.is_even(0)