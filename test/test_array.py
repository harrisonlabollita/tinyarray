import numpy as np
from tinyarray import array as ta
import unittest
import random

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
        y = x/2
        t1 = y.numpy()
        x /= 2
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

    def test_reverse(self):
        random.seed(1234)
        x = ta.array.uniform(10).sort()

        t1 = ta.array([0.007491470058587191, 
                   0.08393822683708396, 
                   0.23680977536311776, 
                   0.4407325991753527, 
                   0.5822275730589491, 
                   0.6715634814879851, 
                   0.7664809327917963, 
                   0.9109759624491242, 
                   0.939268997363764, 
                   0.9664535356921388]).numpy()
        y = x.reverse().numpy()
        np.testing.assert_allclose(y,t1[::-1])

    def test_prod(self):
        x = ta.array([1, 3, 5, 7])
        ans = x.prod()
        self.assertEqual(ans, 105)

    def test_sort(self):
        random.seed(1234)
        x = ta.array.uniform(10)
        x1 = x.sort().numpy()
        x2 = x.argsort().numpy()
        t1 = ta.array([0.007491470058587191, 
                   0.08393822683708396, 
                   0.23680977536311776, 
                   0.4407325991753527, 
                   0.5822275730589491, 
                   0.6715634814879851, 
                   0.7664809327917963, 
                   0.9109759624491242, 
                   0.939268997363764, 
                   0.9664535356921388]).numpy()
        t2 = ta.array([2, 7, 9, 1, 5, 6, 8, 3, 4, 0]).numpy()
        np.testing.assert_allclose(x1, t1)
        np.testing.assert_allclose(x2, t2)

    def test_find(self):
        random.seed(1234)
        x = ta.array.uniform(10)
        t1 = x.find(0.5, func=lambda x, val: x >=val).numpy()
        t2 = ta.array([0.9664535356921388, 0.9109759624491242, 
                    0.939268997363764, 0.5822275730589491, 
                    0.6715634814879851, 0.7664809327917963]).numpy()
        np.testing.assert_allclose(t1, t2)

        t1 = x.find(0.5, func=lambda x, val: x < val).numpy()
        t2 = ta.array([0.4407325991753527, 0.007491470058587191, 0.08393822683708396, 0.23680977536311776]).numpy()
        np.testing.assert_allclose(t1, t2)





if __name__ == "__main__":
    unittest.main()
