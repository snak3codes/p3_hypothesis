from math import isnan
from hypothesis import given, assume
from hypothesis.strategies import floats, integers, lists
from typing import List
from assume_inverse import negation_is_self_inverse

""" 
DOESN'T WORK: Falsifying example: test_negation_is_self_inverse(x=float('nan'))
               AssertionError
@given(floats())
def test_negation_is_self_inverse(x):
    assert x == -(-x) 
"""


@given(floats())
def test_negation_is_self_inverse_for_non_nan(x):  # PASSES
    assume(not isnan(x))  # Assume that x is not a NaN
    assert x == -(-x)


""" How Good Is Assume? """

""" 
DOESN'T WORK: Falsifying example: test_sum_is_positive(
    xs=[],
) --> Empty list fails this test because its sum([]) is 0, which is not > 0 as
our assertion says
@given(lists(integers()))
def test_sum_is_positive(xs: List[int]):
    assert sum(xs) > 0
 """

"""
DOESN'T WORK: Falsifying example: test_sum_is_positive(
    xs=[0],
) --> sum([0]) is 0, which is not > 0 as our assertion says
@given(lists(integers()))
def test_sum_is_positive(xs: List[int]):
    assume(xs)  # We assume that xs is not empty
    assert sum(xs) > 0
 """

# We need a more powerful assumption


@given(lists(integers()))
def test_sum_is_positive(xs: List[int]):
    assume(xs)  # We won't fail on empty list, our assumption keeps us safe
    # Extra Assumption
    assume(all(x > 0 for x in xs))  # We assume every element in xs is > 0
    assert sum(xs) > 0  # This passes because
    # the sum of a non-empty list of positive integers is positive --> True!


if __name__ == '__main__':
    import pytest
    pytest.main(['test_assume.py'])
