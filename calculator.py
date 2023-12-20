class Calculator:
  """A simple calculator class that can perform basic arithmetic operations."""

  def __init__(self):
      """Initialize the calculator with a memory value of 0."""
      self.memory = 0

  def add(self, x):
      """Add a number to the memory value and return the result.

      Args:
          x (float): The number to be added.

      Returns:
          float: The sum of the memory value and x.
      """
      self.memory += x
      return self.memory

  def subtract(self, x):
      """Subtract a number from the memory value and return the result.

      Args:
          x (float): The number to be subtracted.

      Returns:
          float: The difference of the memory value and x.
      """
      self.memory -= x
      return self.memory

  def multiply(self, x):
      """Multiply the memory value by a number and return the result.

      Args:
          x (float): The number to be multiplied.

      Returns:
          float: The product of the memory value and x.
      """
      self.memory *= x
      return self.memory

  def divide(self, x):
      """Divide the memory value by a number and return the result.

      Args:
          x (float): The number to be divided.

      Returns:
          float: The quotient of the memory value and x.

      Raises:
          ZeroDivisionError: If x is zero.
      """
      if x == 0:
          raise ZeroDivisionError("Cannot divide by zero")
      self.memory /= x
      return self.memory

  def root(self, n):
      """Take the n-th root of the memory value and return the result.

      Args:
          n (float): The degree of the root.

      Returns:
          float: The n-th root of the memory value.

      Raises:
          ValueError: If n is zero or negative.
      """
      if n <= 0:
          raise ValueError("Cannot take zero or negative root")
      self.memory **= (1/n)  # Use the ** operator to calculate the nth root
      return self.memory

  def reset(self):
      """Reset the memory value to zero and return it.

      Returns:
          float: The memory value after resetting.
      """
      self.memory = 0
      return self.memory
