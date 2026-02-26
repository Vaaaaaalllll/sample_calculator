# WARNING: template code, may need edits
"""Basic arithmetic operations."""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Add two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    
    Example:
        >>> add(1, 1)
        2
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract b from a.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Divide a by b.
    
    Args:
        a: Numerator
        b: Denominator
    
    Returns:
        Quotient of a and b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
