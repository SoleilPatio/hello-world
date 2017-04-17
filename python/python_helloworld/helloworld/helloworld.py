'''

@author: MTK02679
'''
import sys
import unittest
import urllib


if sys.version_info[0] > 2:
    import urllib.request




class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def _change(self,x):
        x = 100
        
    def testHello(self):
        var = None
        var2 = var
        self._change(var2)
        print var2
    
    
    def XtestName(self):
        url = "https://tw.news.yahoo.com/"
        try:
            response = urllib.urlopen(url)
        except:
            response = urllib.request.urlopen(url)
            
        if sys.version_info[0] > 2:
            encoding = response.headers.get_content_charset('charset')
        else:
            encoding = response.headers.getparam("charset")
        
        print(  "encoding = " + encoding)
        
        html = response.read()
#         
        print(html.decode(encoding).encode(sys.stdin.encoding,"replace").decode(sys.stdin.encoding))
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()