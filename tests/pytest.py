import unittest
from main import *

class TestMain(unittest.TestCase):
    def test_my_func(self):
        self.assertEqual(main, 0)

if __name__ == '__main__':
    unittest.main()
