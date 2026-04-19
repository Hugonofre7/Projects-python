"""
Tests for calculator operations.
Uses pytest for testing.
"""

import pytest
from calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    sqrt,
)


def test_add():
    """Test addition with positive and negative numbers."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 5) == 5
    assert add(2.5, 3.5) == 6.0


def test_subtract():
    """Test subtraction with positive and negative numbers."""
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(-1, -1) == 0
    assert subtract(0, 5) == -5
    assert subtract(5.5, 2.2) == 3.3


def test_multiply():
    """Test multiplication with positive and negative numbers."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(0, 5) == 0
    assert multiply(2.5, 2) == 5.0


def test_divide():
    """Test division with positive and negative numbers."""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 3) == -2
    assert divide(-6, -3) == 2
    
    # Test division by zero
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_power():
    """Test power operations."""
    assert power(2, 3) == 8
    assert power(2, 0) == 1
    assert power(2, -1) == 0.5
    assert power(4, 0.5) == 2.0
    assert power(-2, 2) == 4
    assert power(-2, 3) == -8


def test_sqrt():
    """Test square root operations."""
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    assert sqrt(2) == pytest.approx(1.41421356237)
    assert sqrt(0) == 0
    assert sqrt(0.25) == 0.5
    
    # Test negative numbers
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        sqrt(-1)


def test_divide_by_zero_error_message():
    """Test that division by zero gives correct error message."""
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(5, 0)
    assert str(excinfo.value) == "Cannot divide by zero"
    