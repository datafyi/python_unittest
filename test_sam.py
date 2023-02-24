import unittest
from .sum import sum

class MyTestCase(unittest.TestCase):
    def test_sum(self):
        result = sum(x=2, y=3)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
