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
    """[CLS]: fastest way to copy data, must assign range, or it will repeat"""
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
[REDO]
1.6 Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?
"""
import numpy as np

def _rotate(mat,r,c, dim):
    no1 = mat[r,c]
    
    new_r = c
    new_c = dim - r - 1
    #1
    mat[r,c] = mat[new_r,new_c]
    
    r=new_r
    c=new_c
    new_r = c
    new_c = dim - r - 1
    #2
    mat[r,c] = mat[new_r,new_c]
    
    r=new_r
    c=new_c
    new_r = c
    new_c = dim - r - 1
    #3
    mat[r,c] = mat[new_r,new_c]
    
    r=new_r
    c=new_c
    new_r = c
    new_c = dim - r - 1
    #4
    mat[r,c] = no1
    


    
def rotate_mat_90(mat):
    print mat
    
    (row, col) = mat.shape
    
    for r in range(row/2):
        for c in range(r, col-r-1):
            _rotate(mat,r,c, row)
            
    print mat
            
    
    
def main_rotate_mat_90():
    mat = np.zeros((5,5))
    mat.flat[:] = range(5*5)
    
    rotate_mat_90(mat)
    
    



"""
1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0.
"""
import numpy as np
def set_mat_zero(mat):
    (row, col) = mat.shape
    
    zero_r = {}
    zero_c = {}
    
    for r in range(row):
        for c in range(col):
            if mat[r,c] == 0:
                zero_r[r] = 1
                zero_c[c] = 1
                
    for r in zero_r.keys():
        for c in range(col):
            mat[r,c] = 0
    
    for c in zero_c.keys():
        for r in range(row):
            mat[r,c] = 0
            

def main_set_mat_zero():
    mat = np.zeros((5,4))
    mat.flat[:] = range(5*4)
    
    mat[4,3]=0
    mat[2,2]=0
    print mat
    set_mat_zero(mat)
    print mat



"""
1.8 Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check If s2 is a rotation of s1
using only one call to isSubstring (e.g., "waterbottLe" is a rotation of "erbottLewat").
"""

def isSubstring(s3,s1):
    return True if s3.find(s1) != -1 else -1
    

def is_rotation_of(s1, s2):
    s3 = s2 + s2
    return isSubstring(s3,s1)







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
#     main_rotate_mat_90()
#     main_set_mat_zero()
    print is_rotation_of("waterbottLe", "erbottLewat" )

    
    print "Done"