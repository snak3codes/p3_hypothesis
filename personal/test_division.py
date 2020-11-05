from hypothesis import given, assume
from hypothesis.strategies import integers

from division import divide


@given(integers(), integers().filter(lambda x: x != 0))
def test_divide(a, b):
    assert divide(a, b) == a / b


@given(integers().filter(lambda x: x > 0), integers().filter(lambda x: x > 0))
def test_divide_positive_integers(a, b):
    assert divide(a, b) == a / b


@given(integers().filter(lambda x: x < 0), integers().filter(lambda x: x < 0))
def test_divide_negative_integers(a, b):
    assert divide(a, b) == a / b


@given(integers(), integers())
def test_divide_assume_b_nonzero(a, b):
    """ We can also use "assumptions" """
    assume(b > 0)
    assert divide(a, b) == a / b


if __name__ == "__main__":
    import pytest
    pytest.main(['test_division.py'])
