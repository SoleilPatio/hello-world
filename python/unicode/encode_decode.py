# -*- coding: utf-8 -*-

"""
[CLS]:
    hint:
        str : 是encoded 的
        unicode: 是沒有encoded的(所有decode出來的都是unicode)

    str        --- decode("utf-8") ---> unicode
    unicode    --- encode("utf-8") ---> str
    
    1.only string that have been encoded can be transmitted over something
    2.a unicode string just a mapping of (character<->code point), no business with encoding
    3.a presentation of a unicode string is veried by platforms  
"""
def showinfo(some_str):
    print "type=", type(some_str), "len=", len(some_str),"repr=", repr(some_str), "print=",some_str

if __name__ == '__main__':
    
    """
    [CLS]:In Python 2, you need the leading "u"
          In Python 3, no need to do this because all the string is unicode
    """
    a_unicode_str = u"abc中文字串"
    print "[a_unicode_str]"
    showinfo(a_unicode_str)
    print u"[CLS]:特別指定是unicode編碼"
    print ""
    
    #unicode str ---(encode as utf-8)---> str
    a_utf8_encoded_unicode_str = a_unicode_str.encode("utf-8")
    print "[a_utf8_encoded_unicode_str]"
    showinfo(a_utf8_encoded_unicode_str)
    print u"[CLS]:原unicode str裡面不只有英文,所以編碼如選ascii會失敗"
    print ""
    
    #unicode str ---(encode as big5)---> str
    a_big5_encoded_unicode_str = a_unicode_str.encode("big5")
    print "[a_big5_encoded_unicode_str]"
    showinfo(a_big5_encoded_unicode_str)
    print u"[CLS]:打出亂碼要看console的編碼(Run->Run Config->Common->Encoding), unicode can print out anywhere"
    print ""
    
    
    a_str = "abc中文字串"
    print "[a_str]"
    showinfo(a_str)
    print u"[CLS]:因為檔案指定utf-8編碼，所以是utf-8編碼字串"
    print ""
    
    
    a_big5_encoded_str = 'abc\xa4\xa4\xa4\xe5\xa6r\xa6\xea'
    print "[a_big5_encoded_str]"
    showinfo(a_big5_encoded_str)
    print u"[CLS]:印出亂碼是因為console將big-5 encode解釋成utf-8 encode"
    print ""
    
    a_unicode_from_decode_big5_encoded_str = a_big5_encoded_str.decode("big5")
    print "[a_unicode_from_decode_big5_encoded_str]"
    showinfo(a_unicode_from_decode_big5_encoded_str)
    print u"[CLS]:decode還原回來的都是unicode"
    print ""
    