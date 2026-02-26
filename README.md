# WARNING: template code, may need edits
# Sample Calculator

A simple Python calculator application that performs basic arithmetic operations.

## Features

- Addition, subtraction, multiplication, and division
- Command-line interface
- Extensible architecture for adding new operations
- Comprehensive test coverage

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py
```

Or use it as a module:

```python
from src.calculator import Calculator

calc = Calculator()
result = calc.add(1, 1)
print(result)  # Output: 2
```

## Running Tests

```bash
pytest tests/
```

## Project Structure

```
sample_calculator/
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   ├── operations.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── docs/
│   └── usage.md
├── .gitignore
├── requirements.txt
├── setup.py
└── README.md
```

## License

MIT
