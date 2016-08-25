'''
@author: MTK02679
'''
import unittest

from matplotlib import pyplot as plt
import numpy as np


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