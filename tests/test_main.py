import pytest
import source.main as main


def test_add():
    assert main.add(3, 2) == 5


def test_divide():
    assert main.divide(2, 2) == 1


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        main.divide(2, 0)


def test_multiply():
    assert main.multiply(1, 1) == 1


def test_multiply_by_zero():
    assert main.multiply(1, 0) == 0


def test_multiply_negative():
    assert main.multiply(1, -1) == -1
