import unittest
from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """A test case class for the Calculator class."""

    def setUp(self):
        """Create a Calculator object before each test."""
        self.calc = Calculator()

    def tearDown(self):
        """Delete the Calculator object after each test."""
        del self.calc

    def test_add(self):
        """Test the add method of the Calculator class."""
        self.assertEqual(self.calc.add(2), 2)
        self.assertEqual(self.calc.add(3), 5)
        self.assertEqual(self.calc.add(-1), 4)

    def test_subtract(self):
        """Test the subtract method of the Calculator class."""
        self.assertEqual(self.calc.subtract(2), -2)
        self.assertEqual(self.calc.subtract(3), -5)
        self.assertEqual(self.calc.subtract(-1), -4)

    def test_multiply(self):
        """Test the multiply method of the Calculator class."""
        self.assertEqual(self.calc.multiply(2), 0)
        self.calc.add(1) # Set the memory value to 1
        self.assertEqual(self.calc.multiply(3), 3)
        self.assertEqual(self.calc.multiply(-2), -6)

    def test_divide(self):
        """Test the divide method of the Calculator class."""
        self.assertRaises(ZeroDivisionError, self.calc.divide, 0)
        self.calc.add(1) # Set the memory value to 1
        self.assertEqual(self.calc.divide(2), 0.5)
        self.assertEqual(self.calc.divide(-4), -0.125)

    def test_root(self):
        """Test the root method of the Calculator class."""
        self.assertRaises(ValueError, self.calc.root, 0)
        self.assertRaises(ValueError, self.calc.root, -1)
        self.calc.memory = 4 # Set the memory value to 4
        self.assertEqual(self.calc.root(2), 2)
        self.assertEqual(self.calc.root(4), 1.189207115002721)
        

    def test_reset(self):
        """Test the reset method of the Calculator class."""
        self.assertEqual(self.calc.reset(), 0)
        self.calc.add(5) # Set the memory value to 5
        self.assertEqual(self.calc.reset(), 0)

if __name__ == "__main__":
    unittest.main()
