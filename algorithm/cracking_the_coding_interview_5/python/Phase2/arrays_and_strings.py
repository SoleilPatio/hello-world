"""
1.1 Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?
"""
def partition(arr, start, end):
    
    mid_index = (start + end)/2
    mid_val = arr[mid_index]
    
    while True:
        while arr[start] < mid_val:
            start += 1
            if start == end:
                return start
            
        while arr[end] > mid_val:
            end -= 1
            if start == end:
                return start
        
        #swap start and end
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        
        #check if equal
        if arr[start]==mid_val and arr[end]==mid_val and start != end:
            start += 1
            if start == end:
                return start
            
        
    
    
def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = partition(arr, start, end)
    
    quick_sort(arr, start, pivot-1)
    quick_sort(arr, pivot+1, end) 
    
def check_string_if_unique_char(str_arr):
    quick_sort(str_arr, 0, len(str_arr)-1 )
    print "==>",str_arr
    
    last_c = None
    for c in str_arr:
        if last_c == c:
            return False
        last_c = c
    return True
    
    
    
    
    
def main_check_string_unique_char():
    str1 = list("book")
    str2 = list("CloudsCloudsCloudsCloudsCloudsClouds")
    
    print check_string_if_unique_char(str1)
    print check_string_if_unique_char(str2)
    
    
    


"""
1.2 Implement a function void reverse(char* str) in C or C++ which reverses a null-
terminated string.
"""
def reverse_string(strarr):
    count = len(strarr)
    
    for i in range(count):
        j = count-1-i
        if i >= j:
            break
        temp = strarr[i]
        strarr[i] = strarr[j]
        strarr[j] = temp
    
    return strarr

def main_reverse_str():
    strarr = list("I am Clouds. How are You?!")
    print "".join(strarr),"==>",
    print "".join(reverse_string(strarr))
        
        
"""
1.3 Given two strings, write a method to decide if one is a permutation of the other.
"""
def check_permutation(str1, str2):
    result = True
    map1 = {}
    map2 = {}
    for c in str1:
        if c in map1:
            map1[c] += 1
        else:
            map1[c] = 1
            
    for c in str2:
        if c in map2:
            map2[c] += 1
        else:
            map2[c] = 1
    
    kcount1 = len(map1.keys())
    kcount2 = len(map2.keys())
    
    if kcount1 != kcount2:
        result = False
    else:
        for k in map1:
            value2 = map2.get(k, None)
            if value2 != map1[k]:
                result = False
                break
            
    
    print "\"",str1, "\"", "%s"%"is" if result else "is NOT", "a permutation of", "\"",str2, "\""
                

def main_check_permutation():
    check_permutation("clouds", "sdoucl")
    check_permutation("i am busy", "busy am i")
    check_permutation("abba", "bbff")
    
    
    
    
    

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
  
            
"""
 1.5 Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string.
"""


"""
[REDO]
1.6 Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?
"""



"""
1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0.
"""


"""
1.8 Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check If s2 is a rotation of s1
using only one call to isSubstring (e.g., "waterbottLe" is a rotation of "erbottLewat").
"""


if __name__ == "__main__":
    main_check_string_unique_char()
    main_reverse_str()
    main_check_permutation()
    
    
    print "\nDone!"
