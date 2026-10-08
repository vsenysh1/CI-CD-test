import pytest

from calc import add, divide, multiply


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
        
def test_multiply():
    assert multiply(3, 4) == 12