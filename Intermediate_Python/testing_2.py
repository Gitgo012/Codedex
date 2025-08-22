# Write code below 💖

import unittest

def add(a,b):
  return a+b

class MyTestCase(unittest.TestCase):
  def test_addition(self):
    result=add(2,3)
    self.assertEqual(result, 5)

  def test_string_length(self):
    text="hello world"
    self.assertEqual(len(text),11)

  def test_text_contains_word(self):
    text="hello world"
    self.assertTrue('hello' in text)
    self.assertIn('world', text)

if __name__=="__main__":
  unittest.main()
  
