import numpy as np
from tinyarray import array as ta
import unittest

class TestTinyArray(unittest.TestCase):

    def test_add(self):
        x = ta.array([1,2,3,4])
        y = ta.array([1,2,3,4])
        z = x + y
        t1 = z.numpy()
        x += y
        t2 = x.numpy()
        np.testing.assert_allclose(t1, t2)
    
    def test_mul(self):
        x = ta.array([1,2,3,4])
        y = x*2
        t1 = y.numpy()
        x *= 2
        t2 = x.numpy()
        np.testing.assert_allclose(t1, t2)



if __name__ == "__main__":
    unittest.main()
