import pytest
from discount import calculate_discount


def test_calculate_discount_standard():
    assert calculate_discount(100, 20) == 80.0
    assert calculate_discount(50, 10) == 45.0


def test_calculate_discount_zero_percent():
    assert calculate_discount(100, 0) == 100.0


def test_calculate_discount_hundred_percent():
    assert calculate_discount(100, 100) == 0.0


def test_calculate_discount_invalid_percent():
    with pytest.raises(ValueError):
        calculate_discount(100, -5)
    with pytest.raises(ValueError):
        calculate_discount(100, 105)
