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
        
    def isNumber(self, s):
        import re
        s = s.strip()
        
        print s,
        
        #"."
        if s==".":
            return False
        
        #no any digit
        match = re.search("\d", s)
        if match == None:
            return False
        
        #1
        match = re.match("^[+-]?\d+$", s)
        if match:
            return True
        
        #2.1
        match = re.match("^[+-]?\d*\.\d*$", s)
        if match:
            return True
        
        #2e10
        match = re.match("^[+-]?\d+\.?\d*e[+-]?\d+$", s)
        if match:
            return True
        
        #.21e81
        match = re.match("^([+-]?\d*)\.(\d*)e([+-]?\d+)$", s)
        if match:
            print match.groups()
            if match.group(1)=="" and match.group(2)=="":
                return False
            if match.group(3)=="":
                return False
                
            return True
        
        return False
       
        
        
        
        
        
        
    def testHello(self):
        import re
        print self.isNumber("0")
        print self.isNumber(" 0.1")
        print self.isNumber("abc")
        print self.isNumber("1 a")
        print self.isNumber("2e10")
        print self.isNumber("e")
        print self.isNumber(".1")
        print self.isNumber("-1.")
        print self.isNumber("-.")
        print self.isNumber(".2e81")
        print self.isNumber(".e1")
        
        match = re.match(".(\d)", ".111")
        print "-->", match.group() if match else None
    
    
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