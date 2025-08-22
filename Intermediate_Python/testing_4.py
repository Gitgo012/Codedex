from testing_3 import reverse_string, capitalize_string, is_capitalized
import unittest
class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        result=reverse_string("abcd")
        self.assertEqual(result, "dcba")
        
    def test_capitalize_string(self):
        result=capitalize_string("hello world")
        self.assertEqual(result, "Hello world")
        
    def test_is_capitalized(self):
        result=is_capitalized("hellow")
        self.assertEqual(result, False)
        
        
if __name__=="__main__":
    unittest.main()