'''

@author: clouds
'''

import sys
import unittest
import re

if sys.version_info[0] > 2:
    from urllib.request import urlopen
    from urllib.request import Request
else:
    from urllib import urlopen



from bs4 import BeautifulSoup


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        url="https://tw.news.yahoo.com/"
        req = urlopen(url)
        
        if sys.version_info[0] > 2:
            encoding = req.headers.get_content_charset()
        else:
            encoding = req.headers.getparam("charset")
            
        print("encoding = " + encoding)
        print("sys.stdin.encoding = " + sys.stdin.encoding)
        
        #encoded raw data
        html = req.read()
        
        print("encoded raw data = ")
        print(html) #encoded string (bytes object)
        
        
        #decoded string as sys.stdin
        CP950_content = html.decode(encoding,"replace").encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
#         print("CP950_content sys.in = \n" + CP950_content)
        
        
        #
        #Beautiful soup
        #
        soup = BeautifulSoup(html, 'html.parser')

#         
        print("soup_pretty=")
#         print(soup.prettify())
        #
        #prettify() is a decoded utf-8 str object (cannot be 1-1 map to cp950
        #
#         print(soup.prettify().encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)) ###WHY??? WHY encode to utf-8 can work?? (only told the soup the encoding type is utf-8
#         print( soup.prettify(encoding="utf-8")) ###WHY??? WHY encode to utf-8 can work??

        print(soup.title)
        print(soup.get_text().encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()