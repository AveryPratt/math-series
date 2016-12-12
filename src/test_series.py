"""Tests for fibonacci and lucas sequences."""


import pytest


FIBONACCI_TABLE = [
    [1, 0],
    [2, 1],
    [3, 1],
    [4, 2],
    [5, 3],
    [6, 5],
    [7, 8],
    [8, 13],
]

LUCAS_TABLE = [
    [1, 2],
    [2, 1],
    [3, 3],
    [4, 4],
    [5, 7],
    [6, 11],
    [7, 18],
    [8, 29],
]

SUM_SERIES_TABLE = [
    [1, 0, 2],
    [2, 1, 1],
    [3, 1, 3],
    [4, 2, 4],
    [5, 3, 7],
    [6, 5, 11],
    [7, 8, 18],
    [8, 13, 29],
]


@pytest.mark.parametrize("idx, fib", FIBONACCI_TABLE)
def test_fibonacci(idx, fib):
    """Test for fibonacci sequence."""
    from series import fibonacci
    assert fibonacci(idx) == fib


@pytest.mark.parametrize("idx, luc", LUCAS_TABLE)
def test_lucas(idx, luc):
    """Test for lucas sequence."""
    from series import lucas
    assert lucas(idx) == luc


@pytest.mark.parametrize("idx, fib, luc", SUM_SERIES_TABLE)
def test_sum_series(idx, fib, luc):
    """Test for sum series."""
    from series import sum_series
    assert sum_series(idx) == fib
    assert sum_series(idx, 2, 1) == luc
