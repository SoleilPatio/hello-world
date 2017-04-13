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




if __name__ == "__main__":
    
    print is_all_unique("abcd efgh")
    print reverse_str(list("abcdefgh")) #[CLS]: "abcd" is constant  cannot be modified, use list("abcd")
    print is_permutation("abcd", "bcad")
    print is_permutation2("abcd", "abc")
    
    
    print "Done"