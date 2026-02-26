# WARNING: template code, may need edits
# Calculator Usage Guide

## Overview

The Sample Calculator is a Python application that provides basic arithmetic operations with a simple interface.

## Basic Usage

### As a Command-Line Tool

Run the calculator interactively:

```bash
python src/main.py
```

You'll be presented with a menu:

```
=== Simple Calculator ===
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. View History
6. Clear History
7. Exit
=========================
```

### As a Python Module

Import and use the Calculator class in your Python code:

```python
from src.calculator import Calculator

# Create a calculator instance
calc = Calculator()

# Perform operations
result = calc.add(1, 1)
print(result)  # Output: 2

result = calc.multiply(5, 3)
print(result)  # Output: 15

result = calc.divide(10, 2)
print(result)  # Output: 5.0
```

## Features

### Supported Operations

1. **Addition**: Add two numbers
   ```python
   calc.add(5, 3)  # Returns: 8
   ```

2. **Subtraction**: Subtract second number from first
   ```python
   calc.subtract(10, 4)  # Returns: 6
   ```

3. **Multiplication**: Multiply two numbers
   ```python
   calc.multiply(6, 7)  # Returns: 42
   ```

4. **Division**: Divide first number by second
   ```python
   calc.divide(20, 4)  # Returns: 5.0
   ```

### History Tracking

The calculator automatically tracks all operations:

```python
calc = Calculator()
calc.add(1, 1)
calc.multiply(5, 3)

# View history
history = calc.get_history()
for operation in history:
    print(operation)
# Output:
# 1 + 1 = 2
# 5 * 3 = 15

# Clear history
calc.clear_history()
```

### Error Handling

The calculator handles common errors gracefully:

```python
try:
    calc.divide(10, 0)
except ValueError as e:
    print(e)  # Output: Cannot divide by zero
```

## Advanced Usage

### Using Individual Operations

You can also use the operation functions directly:

```python
from src.operations import add, subtract, multiply, divide

result = add(10, 5)  # Returns: 15
result = multiply(3, 4)  # Returns: 12
```

### Type Hints

All functions support both integers and floats:

```python
calc.add(1, 1)        # Integer input
calc.add(1.5, 2.5)    # Float input
calc.add(1, 2.5)      # Mixed input
```

## Examples

### Example 1: Basic Calculation

```python
from src.calculator import Calculator

calc = Calculator()
result = calc.add(1, 1)
print(f"1 + 1 = {result}")  # Output: 1 + 1 = 2
```

### Example 2: Chain Calculations

```python
calc = Calculator()

# Calculate: (10 + 5) * 2 / 3
step1 = calc.add(10, 5)      # 15
step2 = calc.multiply(step1, 2)  # 30
step3 = calc.divide(step2, 3)    # 10.0

print(f"Result: {step3}")
print(f"History: {calc.get_history()}")
```

### Example 3: Error Handling

```python
calc = Calculator()

try:
    result = calc.divide(100, 0)
except ValueError as e:
    print(f"Error occurred: {e}")
    # Handle the error appropriately
```

## Testing

Run the test suite to verify functionality:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_calculator.py
```

## Tips

- The calculator maintains operation history automatically
- All operations support both integers and floating-point numbers
- Division by zero is handled with a clear error message
- History can be cleared at any time without affecting functionality
