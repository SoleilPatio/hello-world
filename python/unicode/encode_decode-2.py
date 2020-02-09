# -*- coding: utf-8 -*-
#[CLS]:這行讓py source code 可以寫Non-Ascii字元(中文)


#[CLS]: 
#  1. u" " or U" " 是 Unicode literals 
#  2. Unicode literals : 是unicode raw data, 沒有encode過，所以是無法顯示的。直接print s 是不行的
#  3. 要encode過，才能顯示.(utf-8)
#  4. 要跟console一樣的encode,才能在console show出來
s = u"a\xac\u6B63\u80FD\U000091CF"
    #  ^^^^ two-digit hex escape
    #      ^^^^^^ four-digit Unicode escape
    #                  ^^^^^^^^^^ eight-digit Unicode escape

for c in s:  print "[",ord(c),"]",              #[ 97 ] [ 172 ] [ 26112 ] [ 24237 ] [ 32768 ] 
print ""

for c in s:  print "[",c.encode("utf-8"),"]",   #[ a ] [ ¬ ] [ 正 ] [ 能 ] [ 量 ] 
print ""

# for c in s:  print "[",c.encode("utf-16"),"]", #[ ��a ��  : 要跟console一樣的encode,才能在console show出來,否則是亂碼
# print ""

for c in s:  print "[",repr(c),"]",              #[ u'a' ] [ u'\xac' ] [ u'\u6b63' ] [ u'\u80fd' ] [ u'\u91cf' ]    : 印出unicode number
print ""
