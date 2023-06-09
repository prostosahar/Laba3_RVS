import unittest
from main import suum

class TestMain(unittest.TestCase):
    def test_my_func(self):
        self.assertEqual(suum, 0)

if __name__ == '__main__':
    unittest.main()
