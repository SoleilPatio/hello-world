'''
@author: MTK02679
'''
import unittest

from matplotlib import pyplot as plt
import numpy as np

def interpolate_2D():
    from scipy import interpolate

    x = [ 50, 60, 70 ]
    y = [ 2 , 2.5 , 3]
    z = [
        [ 1, 2, 3],
        [ 4, 5, 6],
        [ 7, 8, 9] 
    ]

    # f = interpolate.interp2d(x, y, z, kind='cubic')
    f = interpolate.interp2d(x, y, z, kind='linear', fill_value=None)
    print(f(50,2))
    

    

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testMatplot(self):
        X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
        C, S = np.cos(X), np.sin(X)
        
        plt.plot(X, C)
        plt.plot(X, S)
        
        plt.show()
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
