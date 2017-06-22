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
def encode_string(strarr):
    space_count = 0
    len_count = 0
    for c in strarr:
        len_count += 1
        if c == " ":
            space_count += 1
        if c == "":
            break
    
    total_count = len_count + space_count*2
    print len_count
    print total_count;
    
    rp = len_count-1
    wp = total_count-1
    while rp >0 and wp > 0 and rp != wp:
        if(strarr[rp]==" "):
            strarr[wp]="0"
            wp-=1
            strarr[wp]="2"
            wp-=1
            strarr[wp]="%"
            wp-=1
        else:
            strarr[wp] = strarr[rp]
            wp -= 1

        rp -= 1
        
    return strarr
        


def main_encode_string():
    import numpy as np
    str = "Mr John Smith"
    strarr = np.zeros(len(str)*3, dtype="c")
    strarr[0:len(str)] = list(str)
    
    print strarr
    print "".join(encode_string(strarr))
    
            
"""
[CLS]: string += sub_string ==> memory copy O(n)
     use list.append() to do this with O(1)
 1.5 Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string.
"""
def compress_str(string):
    origin_len = len(string)
    
    re_string = ""
    
    last_c = None
    c_count = 0
    for i,c in enumerate(string):
        if ( c != last_c and last_c != None):
            re_string += last_c
            re_string += str(c_count)
            last_c = c
            c_count = 1
        elif i == origin_len-1:
            re_string += c
            re_string += str(c_count+1)
            
        else:
            last_c = c
            c_count += 1
            
    new_len = len(re_string)
    
    if new_len < origin_len:
        return re_string
    else:
        return string
    
def main_compress_str():
    print  compress_str("aabcccccaaa")
            
            
            
        
    


"""
[REDO]
1.6 Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?
"""
def overwrite_index(i, j, N):
    return ( j, N-1-i)
    
    
def rotate_matrix(mat, level=0):
    N,N = mat.shape
    if level > N/2-1:
        return
    
    range_n = N-2*level
    
    for i in range(range_n-1):
        cx , cy = ( 0, i)
        #backup
        temp = mat[cx+level][cy+level]
        #L->U
        (nx,ny) = overwrite_index(cx,cy,range_n)
        mat[cx+level][cy+level] = mat[nx+level][ny+level]
        print cx,cy,nx,ny
        #B->L
        cx, cy = nx, ny
        (nx,ny) = overwrite_index(cx,cy,range_n)
        mat[cx+level][cy+level] = mat[nx+level][ny+level]
        print cx,cy,nx,ny
        #R->B
        cx, cy = nx, ny
        (nx,ny) = overwrite_index(cx,cy,range_n)
        mat[cx+level][cy+level] = mat[nx+level][ny+level]
        print cx,cy,nx,ny
        #U->R
        cx, cy = nx, ny
        (nx,ny) = overwrite_index(cx,cy,range_n)
        mat[cx+level][cy+level] = temp
        print cx,cy,nx,ny
        
        print mat
        
    rotate_matrix(mat, level+1)
    
    
        
def main_rotate_matrix():
    import numpy as np
    mat = np.zeros((5,5),dtype="i4")

    mat = np.array( [[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20],
                     [21,22,23,24,25]] )

    

    print mat
    rotate_matrix(mat)
    print "====>"
    print mat
        




"""
1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0.
"""
def clear_matrix(mat):
    M,N = mat.shape
    
    r_list = []
    c_list = []
    
    for r in range(M):
        for c in range(N):
            item = mat[r][c]
            if item == 0:
                r_list.append(r)
                c_list.append(c)
    
    for r in r_list:
        for c in range(N):
            mat[r][c] = 0
        
    for c in c_list:
        for r in range(M):
            mat[r][c] = 0
            
        
def main_clear_mat():
    import numpy as np
    
    mat = np.array(
        [[0,1,2,3,4,5],
        [1,1,2,3,4,5],
        [1,1,0,3,4,5],
        [1,1,2,3,4,5],
        [1,1,2,3,0,5]]
        )
    
    print mat
    clear_matrix(mat)
    print mat 
    
    


"""
1.8 Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check If s2 is a rotation of s1
using only one call to isSubstring (e.g., "waterbottLe" is a rotation of "erbottLewat").
"""
def isSubstring(s1,s2):
    return s2 in s1
    
    
def check_if_rotation(s1, s2):
    s = s1+s1
    return isSubstring(s,s2)
    
def main_check_if_substring():
    print check_if_rotation("waterbottLe", "erbottLewat")


if __name__ == "__main__":
#     main_check_string_unique_char()
#     main_reverse_str()
#     main_check_permutation()
#     main_encode_string()
#     main_compress_str()
#     main_rotate_matrix()
#     main_clear_mat()
    main_check_if_substring()
    

    
    
    
    
    print "\nDone!"
