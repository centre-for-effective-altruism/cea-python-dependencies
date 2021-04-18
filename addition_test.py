from addition import addition
import unittest

# These tests are here as a starting point, they are not comprehensive
class Testing(unittest.TestCase):
    def test_basics(self):
      self.assertEqual(addition(4, 5), 9)
      
if __name__ == '__main__':
    unittest.main()