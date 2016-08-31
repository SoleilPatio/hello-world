'''

@author: MTK02679
'''
import unittest
import urllib

import urllib.request
import sys


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        url = "https://tw.news.yahoo.com/"
        try:
            response = urllib.urlopen(url)
        except:
            response = urllib.request.urlopen(url)
            
        encoding = response.headers.get_content_charset('charset')
        
        print(  "encoding = " + encoding)
        
        html = response.read()
#         
        print(html.decode(encoding).encode(sys.stdin.encoding,"replace").decode(sys.stdin.encoding))
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()