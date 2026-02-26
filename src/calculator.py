# WARNING: template code, may need edits
"""Calculator class for performing arithmetic operations."""

from typing import Union
from src.operations import add, subtract, multiply, divide

Number = Union[int, float]


class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator."""
        self.history = []

    def add(self, a: Number, b: Number) -> Number:
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            Sum of a and b
        """
        result = add(a, b)
        self._record_operation(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: Number, b: Number) -> Number:
        """Subtract b from a.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            Difference of a and b
        """
        result = subtract(a, b)
        self._record_operation(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: Number, b: Number) -> Number:
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            Product of a and b
        """
        result = multiply(a, b)
        self._record_operation(f"{a} * {b} = {result}")
        return result

    def divide(self, a: Number, b: Number) -> Number:
        """Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
        
        Returns:
            Quotient of a and b
        
        Raises:
            ValueError: If b is zero
        """
        result = divide(a, b)
        self._record_operation(f"{a} / {b} = {result}")
        return result

    def _record_operation(self, operation: str) -> None:
        """Record operation in history.
        
        Args:
            operation: String representation of the operation
        """
        self.history.append(operation)

    def get_history(self) -> list:
        """Get calculation history.
        
        Returns:
            List of previous calculations
        """
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()
