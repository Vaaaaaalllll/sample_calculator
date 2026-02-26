# WARNING: template code, may need edits
"""Unit tests for the calculator module."""

import pytest
from src.calculator import Calculator
from src.operations import add, subtract, multiply, divide


class TestOperations:
    """Test individual operation functions."""

    def test_add(self):
        """Test addition operation."""
        assert add(1, 1) == 2
        assert add(5, 3) == 8
        assert add(-1, 1) == 0
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract(self):
        """Test subtraction operation."""
        assert subtract(5, 3) == 2
        assert subtract(1, 1) == 0
        assert subtract(0, 5) == -5
        assert subtract(10.5, 0.5) == 10.0

    def test_multiply(self):
        """Test multiplication operation."""
        assert multiply(2, 3) == 6
        assert multiply(5, 0) == 0
        assert multiply(-2, 3) == -6
        assert multiply(0.5, 4) == 2.0

    def test_divide(self):
        """Test division operation."""
        assert divide(6, 3) == 2
        assert divide(5, 2) == 2.5
        assert divide(10, 4) == 2.5
        assert divide(-6, 2) == -3

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)


class TestCalculator:
    """Test Calculator class."""

    def test_calculator_add(self):
        """Test calculator addition method."""
        calc = Calculator()
        assert calc.add(1, 1) == 2
        assert calc.add(10, 5) == 15

    def test_calculator_subtract(self):
        """Test calculator subtraction method."""
        calc = Calculator()
        assert calc.subtract(10, 5) == 5
        assert calc.subtract(1, 1) == 0

    def test_calculator_multiply(self):
        """Test calculator multiplication method."""
        calc = Calculator()
        assert calc.multiply(3, 4) == 12
        assert calc.multiply(5, 0) == 0

    def test_calculator_divide(self):
        """Test calculator division method."""
        calc = Calculator()
        assert calc.divide(10, 2) == 5
        assert calc.divide(7, 2) == 3.5

    def test_calculator_divide_by_zero(self):
        """Test calculator division by zero."""
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.divide(5, 0)

    def test_history_recording(self):
        """Test that operations are recorded in history."""
        calc = Calculator()
        calc.add(1, 1)
        calc.subtract(5, 3)
        
        history = calc.get_history()
        assert len(history) == 2
        assert "1 + 1 = 2" in history[0]
        assert "5 - 3 = 2" in history[1]

    def test_clear_history(self):
        """Test clearing calculation history."""
        calc = Calculator()
        calc.add(1, 1)
        calc.multiply(2, 3)
        
        assert len(calc.get_history()) == 2
        
        calc.clear_history()
        assert len(calc.get_history()) == 0

    def test_history_immutability(self):
        """Test that getting history returns a copy."""
        calc = Calculator()
        calc.add(1, 1)
        
        history = calc.get_history()
        history.append("fake operation")
        
        # Original history should be unchanged
        assert len(calc.get_history()) == 1
