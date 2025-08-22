# The .assertRaises() method is great for ensuring that if an edge case exists, the proper error is raised.

# For example, in testing a function that should only accept string inputs, you can use .assertRaises() to verify that passing a non-string value raises a TypeError:

# Passing a non-string will raise a TypeError
# with self.assertRaises(TypeError):
#   self.assertIn('World', 123)

# The .assertRaises() method works as a code block started by the with keyword. Inside the block, we can write tests that might raise an error, such as a TypeError. In this example, the code trying to check if the string 'World' is inside 123. Since 123 is a number, not a string, Python will raise a TypeError.

import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b
class TestUnexpected(unittest.TestCase):
    def test_get_sqrt(self):
        result=get_sqrt(9)
        self.assertEqual(result, 3)
        
    # test edge cases
    def test_negative_number(self):
        with self.assertRaises(ValueError):
            get_sqrt(-9)
            
    def test_divide(self):
        result=divide(144,12)
        self.assertEqual(result, 12)
        
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(12,0)
            
if __name__=="__main__":
    unittest.main()