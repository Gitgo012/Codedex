# Write code below 💖
#Unit testing involves taking smaller pieces of a large program and checking that the code behaves as expected under various scenarios. A unit of code can be as simple as a small function or as complex as a large class.
#In Python, the unittest framework is a built-in module. It helps developers validate the behavior of their code, piece by piece. By isolating and testing each unit independently, we can verify their functionality and behavior.

#A unittest can be as simple as testing that values are the same. We use .assertEqual in unittest to ensure two elements are equal to each ot
# example
#assertEqual(a, b)
## a == b
import unittest

def add(a, b):
  return a + b

class TestAddition(unittest.TestCase):
  # Define the first unit test
  def test_add(self):
    result = add(3, 4)

    # Define the expected result
    expected_result = 7
    self.assertEqual(result, expected_result)

if __name__ == '__main__':
  unittest.main()