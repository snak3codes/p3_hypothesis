from hypothesis import given
from hypothesis.strategies import integers, floats, lists, tuples

from filename import functions  # Import all the functions you are testing on


@given(strategy)
def test(args):
    assert


if __name__ == '__main__':
    import pytest
    pytest.main(['hypo_template.py'])  # Change this to your filename
