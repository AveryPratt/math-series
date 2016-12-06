"""Test for fibonacci and lucas sequences."""


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


@pytest.mark.parametrize("m, n", FIBONACCI_TABLE)
def test_fibonacci(m, n):
    """Test for fibonacci sequence."""
    import series
    assert series.fibonacci(m) == n


def test_lucas():
    """Test for lucas sequence."""
    import series
    assert series.lucas(1) == 2
    assert series.lucas(2) == 1
    assert series.lucas(3) == 3
    assert series.lucas(4) == 4
    assert series.lucas(5) == 7
    assert series.lucas(6) == 11
    assert series.lucas(7) == 18
    assert series.lucas(8) == 29


def test_sum_series():
    """Test for sum series."""
    import series
    assert series.sum_series(1) == 0
    assert series.sum_series(2) == 1
    assert series.sum_series(3) == 1
    assert series.sum_series(4) == 2
    assert series.sum_series(5) == 3
    assert series.sum_series(6) == 5
    assert series.sum_series(7) == 8
    assert series.sum_series(8) == 13
