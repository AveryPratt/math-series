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


def test_sum_series():
    """Test for sum series."""
