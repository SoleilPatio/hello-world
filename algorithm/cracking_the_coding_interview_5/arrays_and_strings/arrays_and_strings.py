"""
1.1 Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?
"""

def is_all_unique(str):
    import numpy as np
    chart_set = np.zeros(256)
    
    for c in str:
        asc = ord(c)
        if chart_set[asc] == 1:
            return False
        else:
            chart_set[asc] = 1

        
    return True    

"""
1.2 Implement a function void reverse(char* str) in C or C++ which reverses a null-
terminated string.
"""
def reverse_str(string):
    count = len(string)
    
    for i in range(0, count/2):
        #swap char
        swap = string[i]
        string[i] = string[count-1-i]
        string[count-1-i] = swap
        
    print string
    print "".join(string)
        
        
"""
1.3 Given two strings, write a method to decide if one is a permutation of the other.
"""


def is_permutation(string1, string2):
    str1 = list(string1)
    str2 = list(string2)
    
    str1.sort()
    str2.sort()
    return str1 == str2

def is_permutation2(string1, string2):
    import numpy
    
    str1 = list(string1)
    str2 = list(string2)
    
    if( len(str1) != len(str2)):
        return False
    
    char_set = numpy.zeros(256)
    
    for c in str1:
        char_set[ord(c)] += 1
        
    for c in str2:
        char_set[ord(c)] -= 1
        if(char_set[ord(c)] < 0):
            return False
    
    print "char_set:", char_set
    return True


"""
1.4 Write a method to replace all spaces in a string with'%20'. You may assume that
the string has sufficient space at the end of the string to hold the additional
characters, and that you are given the "true" length of the string. (Note: if imple-
menting in Java, please use a character array so that you can perform this opera-
tion in place.)
EXAMPLE
Input: "Mr John Smith
Output: "Mr%20Dohn%20Smith"
"""
def replace_space(string):
    import numpy as np
    
    #1) simulate c string
    str_len = len(string)
    """[CLS]: 'a' means ascii"""
    str_buf = np.zeros(3*str_len, dtype='a')
    """[CLS]: fastest way to copy data, must assign range"""
    str_buf[0:str_len] = list(string)
    print "".join(str_buf)
    
    #2) 2-pass algorithm
    result_len = 0
    for c in str_buf:
        if c == '':
            break
        if c ==' ':
            result_len += 3 #%20
        else:
            result_len += 1 #other character
    
    #process from the end
    str_i = str_len-1
    loc_i = result_len-1
    
    while(str_i >= 0):
        if str_buf[str_i]==' ':
            str_buf[loc_i] = '0'
            str_buf[loc_i-1] = '2'
            str_buf[loc_i-2] = '%'
            str_i -= 1
            loc_i -= 3
        else:
            str_buf[loc_i] = str_buf[str_i]
            str_i -= 1
            loc_i -= 1
    
    #3)show result
    print "".join(str_buf)
            
            
"""
 1.5 Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string.
"""
def compress_bad(string):
    ret=""
    
    count = 0
    last_c = None
    for c in string:
        if last_c != c and last_c != None:
            if count > 1:
                """[CLS]: string concatenate cost O(n^2)"""
                ret = ret + last_c + str(count)
            elif count == 1:
                ret = ret + last_c
            count = 0
            
        last_c = c
        count += 1
        
    if count > 1:
        ret = ret + last_c + str(count)
    elif count == 1:
        ret = ret + last_c
    
            
    if len(ret) < len(string):
        return ret
    else:
        return string
    
def compress_good(string):
    ret=[]
    
    count = 0
    last_c = None
    for c in string:
        if last_c != c and last_c != None:
            if count > 1:
                """[CLS]: string concatenate cost O(n^2)"""
                ret.append(last_c + str(count))
            elif count == 1:
                ret.append(last_c)
            count = 0
            
        last_c = c
        count += 1
        
    if count > 1:
        ret.append(last_c + str(count))
    elif count == 1:
        ret.append(last_c)
    
            
    if len(ret) < len(string):
        return "".join(ret)
    else:
        return string    
    
        
        

"""
1.6 Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?
"""

"""
1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0.
pg
"""

loop_count = 100

def method1():
    out_str = ''
    for num in xrange(loop_count):
        out_str += 'num'
    return out_str

def method4():
    str_list = []
    for num in xrange(loop_count):
        str_list.append('num')
    return ''.join(str_list)           
    
    
def foo(arg):
    pass

if __name__ == "__main__":
    import timeit
    
#     print is_all_unique("abcd efgh")
#     print reverse_str(list("abcdefgh")) #[CLS]: "abcd" is constant  cannot be modified, use list("abcd")
#     print is_permutation("abcd", "bcad")
#     print is_permutation2("abcd", "abc")
#     print replace_space("I am Clouds ")
#     print timeit.timeit("compress_bad('aabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaa')", setup="from __main__ import compress_bad")
#     print timeit.timeit("compress_good('aabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaaaabcccccaaa')", setup="from __main__ import compress_good")
#     print timeit.timeit("foo('aabcccccaaa')", setup="from __main__ import foo")
#     print compress_good('aabcccccaaa')
    
    print timeit.timeit("method1()", setup="from __main__ import method1")
    print timeit.timeit("method4()", setup="from __main__ import method4")
    
    print "Done"