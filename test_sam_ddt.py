import unittest
import ddt
from .sum import sum
import itertools
import unittest

from ddt import ddt, data, file_data, idata, unpack

@ddt
class MyTestCase(unittest.TestCase):
    @data((1,2),(-1,3))
    @unpack
    def test_sum(self,x,y):
        result = sum(x, y)
        self.assertEqual(result, x+y)


if __name__ == '__main__':
    unittest.main()
