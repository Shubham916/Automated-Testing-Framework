import unittest
from src.your_code import add, subtract

class TestYourIntegration(unittest.TestCase):
    def test_add_integration(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_subtract_integration(self):
        self.assertEqual(subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()
