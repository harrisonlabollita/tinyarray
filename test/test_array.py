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
    
    def test_sub(self):
        x = ta.array([1,2,3,4])
        y = ta.array([1,2,3,4])
        z = x - y
        t1 = z.numpy()
        x -= y
        t2 = x.numpy()
        np.testing.assert_allclose(t1, t2)
    
    def test_div(self):
        x = ta.array([1,2,3,4])
        y = x*2
        t1 = y.numpy()
        x *= 2
        t2 = x.numpy()
        np.testing.assert_allclose(t1, t2)
    
    def test_mul(self):
        x = ta.array([1,2,3,4])
        y = x*2
        t1 = y.numpy()
        x *= 2
        t2 = x.numpy()
        np.testing.assert_allclose(t1, t2)
        z = x*x
        t3 = z.numpy()
        a = x**2
        t4 = a.numpy()
        np.testing.assert_allclose(t3, t4)

    def test_sum(self):
        x = ta.array([1,2,3,4])
        ans = x.sum()
        self.assertEqual(ans, 10)
        x = ta.array([1.,2.,3.,4.])
        ans = x.sum()
        self.assertEqual(ans, 10.)

    def test_mean(self):
        x = ta.array([1, 3, 5, 7])
        ans = x.mean()
        self.assertEqual(ans, 4)



if __name__ == "__main__":
    unittest.main()
