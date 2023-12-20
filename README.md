# Calculator Package

The Calculator package is a simple Python package that provides a `Calculator` class for performing basic arithmetic operations.

## Installation

To install the Calculator package, you can download the source code from the repository and then install it using pip. Here's how you can do it:

```bash
git clone https://github.com/yourusername/calculator.git
cd calculator
pip install .
```

Replace `'https://github.com/yourusername/calculator.git'` with the actual URL of your repository.

## Usage

Here's how you can use the `Calculator` class in your Python code:

```python
from calculator.calculator import Calculator

# Create a Calculator object
calc = Calculator()

# Perform addition
calc.add(2)

# Perform subtraction
calc.subtract(1)

# Perform multiplication
calc.multiply(3)

# Perform division
calc.divide(2)

# Take the square root
calc.root(2)

# Reset memory
calc.reset()
```

## Methods

The `Calculator` class provides the following methods:

- `add(x)`: Adds `x` to the memory value and returns the result.
- `subtract(x)`: Subtracts `x` from the memory value and returns the result.
- `multiply(x)`: Multiplies the memory value by `x` and returns the result.
- `divide(x)`: Divides the memory value by `x` and returns the result. Raises `ZeroDivisionError` if `x` is zero.
- `root(n)`: Takes the `n`-th root of the memory value and returns the result. Raises `ValueError` if `n` is zero or negative.
- `reset()`: Resets the memory value to zero and returns it.

## Contributing

Contributions are welcome! Please read the contributing guidelines before making any changes.

## License

This project is licensed under the terms of Turing College.