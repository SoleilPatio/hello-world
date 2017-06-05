"""
Bubble Sort
"""


"""
Merge Sort
"""

    
"""
Quick Sort
"""

    
"""
Radix sort
"""


"""
11.1 You are given two sorted arrays, A and B,where A has a large enough buffer at
the end to hold B. Write a method to merge B into A in sorted order.
"""
import numpy as np
def merge_ab(A,sizea,B,sizeb):
    i_last = sizea + sizeb - 1
    i_a = sizea-1
    i_b = sizeb-1
    
    while i_a > 0 and i_b > 0:
        if A[i_a] > B[i_b]:
            A[i_last] = A[i_a]
            i_a -= 1
            i_last -= 1
        else:
            A[i_last] = B[i_b]
            i_b -= 1
            i_last -= 1
            
            
def main_merge_ab():
    sizea = 10
    sizeb = 5
    A = np.zeros(sizea+sizeb)
    A[:sizea] = sorted(np.random.randint(100,size=sizea))
    B = np.zeros(sizeb)
    B[:sizeb] = sorted(np.random.randint(100,size=sizeb))
    
    print "A=",A
    print "B=",B
    merge_ab(A,sizea,B,sizeb)
    print "A=",A
    print "B=",B
    

    


"""
11.2 Write a method to sort an array of strings so that all the anagrams are next to
each other.
"""
def compare_str(ls,rs):
    sl = "".join(sorted(ls))
    sr = "".join(sorted(rs))
    
    if sl < sr:
        return -1
    elif sl == sr:
        return 0
    else:
        return 1
    
    
    

def merge(left,right):
    ret = []
    
    
    cl = len(left)
    cr = len(right)
    
    if cl == 0:
        return right
    elif cr == 0:
        return left
    
    il = 0
    ir = 0
    while True:
        ls = left[il]
        rs = right[ir]
        
        cmp = compare_str(ls,rs)
        
        if cmp <= 0:
            ret.append(ls)
            il += 1
        else:
            ret.append(rs)
            ir += 1
            
        if il >= cl:
            ret.extend(right[ir:])
            return ret
        if ir >= cr:
            ret.extend(left[il:])
            return ret
        
        
        
    
    
def merge_sort_str(str_list):
    
    mid = len(str_list)/2
    
    print mid,
    print str_list
    
    if mid == 0:
        return str_list
    
   
    
    left = merge_sort_str(str_list[0:mid])
    right = merge_sort_str(str_list[mid:])

    
    ret_list = merge(left,right)
    return ret_list



def main_sort_str():
    str_list = [
        "abcde",
        "12345",
        "xyzza",
        "zxyaz",
        "53421",
        "bcdae"
        ]
    
    ret = merge_sort_str(str_list)
    
    print ret
    


"""
11.3 Given a sorted array of n integers that has been rotated an unknown number of
times, write code to find an element in the array. You may assume that the array
was originally sorted in increasing order.
EXAMPLE
Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
Output: 8 (the index of 5 in the array)
"""

"""
11.4 Imagine you have a 20 GB file with one string per line. Explain how you would
sort the file.
"""

"""
11.5 Given a sortedarray of strings which is interspersed with empty strings,write a
method to find the locationof a given string.
EXAMPLE
Input: find "ball" in {"at", "", "", "", "ball", "", "", "car","","","dad","",""}

Output: 4
"""



"""
11.6 Given an MxN matrix in which each row and each column is sorted in ascending
order, write a method to find an element.
"""



"""
11.7 A circus is designing a tower routine consisting of people standing atop one
another's shoulders.For practical and aesthetic reasons, each person must be
both shorter and lighter than the person below him or her. Given the heights
and weights of each person in the circus, write a method to compute the largest
possible number of people in such atower.
EXAMPLE:
Input (ht,wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95)
(68, 110)
Output:The longest tower is length 6 and includes from top to bottom:
(56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)
"""


"""
11.8 Imagine you are readingin a stream of integers.Periodically, you wish to beable
to look up the rank of a number x (the number of values less than or equal tox).
Implement the data structures and algorithms to support these operations.That
is, implement the method track(int x), which is called when each number
is generated, and the method getRankOfNumber(int x), which returns the
number of values less than or equal to x (not including x itself).
EXAMPLE
Stream (inorder of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
getRankOfNumber(l) = 0
getRankOfNumber(3) = 1
getRankOfNumber(4) = 3
"""
def modify(list):
    for i,data in enumerate(list):
        list[i] = "X"
        
    
    
if __name__ == "__main__":
#     main_merge_ab()
#     main_sort_str()

    list = [0,1,2,3,4,5,6,7]
    print list[5:]
    modify(list[5:])
    print list
    modify(list)
    print list
    
    list[5:] = [9,9,9]
    print list
    
    print "\nDone"
