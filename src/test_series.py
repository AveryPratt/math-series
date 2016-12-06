"""Test for fibonacci and lucas sequences."""


import pytest


def test_fibonacci():
    """Test for fibonacci sequence."""
    import series
    assert series.fibonacci(1) == 0
    assert series.fibonacci(2) == 1
    assert series.fibonacci(3) == 1
    assert series.fibonacci(4) == 2
    assert series.fibonacci(5) == 3
    assert series.fibonacci(6) == 5
    assert series.fibonacci(7) == 8
    assert series.fibonacci(8) == 13


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
