"""
Bubble Sort
"""

def bubble_sort(in_list):
    
    
    count = len(in_list)
    
    bigO = 0
    while True:
        b_swap = False
        for i in range(count-1):
            bigO += 1
            if in_list[i] > in_list[i+1]:
                temp = in_list[i]
                in_list[i] = in_list[i+1]
                in_list[i+1] = temp
                b_swap = True
        print in_list    
        if b_swap == False:
            break
        
    print "bigO:", bigO

def main_bubble_sort():
    print "Bubble Sort"
    import numpy as np
    A = np.random.randint(100,size=10)
#     A = list(reversed([10,9,8,7,6,5,4,3,2,1]))
    print A,"==>"
    bubble_sort(A)
    print A
    

"""
Merge Sort
"""

def merge_sort(in_list, start, end):
    if start >= end:
        return
    
    mid = (start + end) / 2
    merge_sort(in_list,start, mid )
    merge_sort(in_list,mid+1, end )
    
    left = list(in_list[start:mid+1])
    right = list(in_list[mid+1:end+1])
    
    #merge
    for i in range(start, end+1):
        merge_sort.bigO += 1
        if left and right:
            if left[0] > right[0]:
                in_list[i] = right[0]
                del right[0]
            else:
                in_list[i] = left[0]
                del left[0]
        elif left==[]:
            in_list[i:end+1] = right[:]
            break
        elif right==[]:
            in_list[i:end+1] = left[:]
            break
    print in_list
        
    
merge_sort.bigO = 0         
        
def main_merge_sort():
    import numpy as np
    print "Merge Sort"
    
    A = np.random.randint(100,size=10)
    print A,"==>"
    merge_sort(A, 0, len(A)-1)
    print "bigO=",merge_sort.bigO
    print A
    
    
"""
Quick Sort
"""

def partition(arr, start, end):

    mid = arr[(start+end)/2]
    
    print "mid=",mid
    
    while start < end:
        print "\t",start,end, arr
        while arr[start] < mid:
            partition.bigO += 1
            start += 1
            if start == end:
                print start,arr
                return start
            
        while arr[end] > mid:
            partition.bigO += 1
            end -= 1
            if end == start:
                print end,arr
                return end
            
        #swap
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        
        
        #handle the num is not unique
        if arr[start] == arr[end]:
            start += 1
            if start == end:
                print start,arr
                return start
            
            
partition.bigO = 0    



def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = partition(arr, start, end)

    quick_sort(arr, start, pivot-1)
    quick_sort(arr, pivot+1, end)
    
    
    
    
def main_quick_sort():
    import numpy as np
    arr = np.random.randint(100,size=10)
    arr = [90, 49, 23, 54, 88, 29, 23,  5, 38, 28]
#     arr = [3, 2, 4, 1, 7, 6, 5,  9, 8, 10]
    arr = [40, 61, 32, 82, 65, 17 ,28, 26, 19, 64]
    print "Quick Sort"
    print arr,"===>"
    quick_sort(arr, 0, len(arr)-1)
    print "bigO=",partition.bigO
    print arr
    
    
"""
Radix sort
"""
def digit(num, level):
    return num%10**level/10**(level-1)
    
    
    
    
    
def radix_sort(arr):
    import collections
    
    for level in range(1,3):
        map = {}
        for key in range(0,10):
            map[key] = collections.deque()
        
        for i in arr:
            key = digit(i,level)
            map[key].append(i)
            
        i = 0
        for key in sorted(map.keys()):
            while map[key]:
                radix_sort.bigO += 1
                arr[i] = map[key].popleft()
                i += 1

radix_sort.bigO = 0        
    
    
def main_radix_sort():
    import numpy as np
    arr = np.random.randint(100,size=10)
    print "Radix Sort"
    print arr,"===>"
    radix_sort(arr)
    print "bigO=",radix_sort.bigO
    print arr



import collections
def radix_sort_msd(arr, start, end, level):
    if level == 0 or start >= end:
        return
    
    bucket = [collections.deque()] * 10
    bucket = [ collections.deque() for _ in range(10) ]
    
    for num in arr[start:end+1]:
        key = digit(num, level)
        bucket[key].append(num)
        radix_sort_msd.bigO += 1
        
    startindex = start
    for q in bucket:
        pointer = startindex
        while q:
            num = q.popleft()
            arr[pointer] = num
            pointer += 1
        radix_sort_msd(arr, startindex, pointer-1, level-1 )
        startindex = pointer
        
    print arr
            
radix_sort_msd.bigO = 0    
    
    
def main_radix_sort_msd():
    import numpy as np
    arr = np.random.randint(100,size=10)
    print "Radix Sort MSD"
    print arr,"===>"
    radix_sort_msd(arr, 0, len(arr)-1, 2)
    print "bigO=",radix_sort_msd.bigO
    print arr    
    
    
    

"""
11.1 You are given two sorted arrays, A and B,where A has a large enough buffer at
the end to hold B. Write a method to merge B into A in sorted order.
"""
def merge_sorted_array( arrA, sizeA, arrB, sizeB ):
    pLast = sizeA + sizeB - 1
    
    pA = sizeA - 1
    pB = sizeB - 1
    
    while pA >= 0 and pB >= 0:
        A = arrA[pA]
        B = arrB[pB]

        if A > B:
            arrA[pLast] = A 
            pA -= 1
        else:
            arrA[pLast] = B 
            pB -= 1
        pLast -= 1
        
def main_merge_sorted_array():
    import numpy as np
    
    sizeA = 10
    sizeB = 5
    
    arrA = np.zeros(sizeA+sizeB)
    arrB = np.zeros(sizeB)
    
    arrA[0:sizeA] = range(sizeA)
    arrB[:] = range(sizeB)
    
    print arrA
    print arrB
    merge_sorted_array(arrA, sizeA, arrB, sizeB)
    print arrA
    
    
    
    
    
    
    


"""
11.2 Write a method to sort an array of strings so that all the anagrams are next to
each other.
"""
class mystring(object):
    def __init__(self, inistr ):
        self.str = inistr
        self.sorted_str_list = sorted(list(inistr))
        
    def compare(self,other):
        for i1, c1 in enumerate(self.sorted_str_list):
            if i1 >= len(other.sorted_str_list):
                return 1 #greater than
            
            if c1 > other.sorted_str_list[i1]:
                return 1
            elif c1 < other.sorted_str_list[i1]:
                return -1 #less than
            
        if len(other.sorted_str_list) > len(self.sorted_str_list):
            return -1
        
        return 0 #equal
    
    
def strpartition(strarr, start, end):
    mid = strarr[(start+end)/2]
    
    while start < end:
        while strarr[start].compare(mid) == -1: #<
            start += 1
            if start == end:
                return start
        while strarr[end].compare(mid) == 1: #>
            end -= 1
            if start == end:
                return start
        
        #swap
        temp = strarr[start]
        strarr[start] = strarr[end]
        strarr[end] = temp
        
        #handle identitly
        if strarr[start].compare(strarr[end]) == 0:
            start += 1
            if start == end:
                return start
            

    
def sort_anagram_strings(strarr, start, end):
    if start >= end:
        return
        
    pivot = strpartition(strarr, start, end)
    
    sort_anagram_strings(strarr, start, pivot-1)
    sort_anagram_strings(strarr, pivot+1, end)
    
    
    
def main_sort_anagram_strings():
    strarr = [
        mystring("clouds"),
        mystring("book"),
        mystring("desk"),
        mystring("oudscl"),
        mystring("oobk"),
        mystring("skde")
        ]
    
    sort_anagram_strings(strarr, 0, len(strarr)-1)
    
    for str in strarr:
        print str.str
    

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
def bin_search(arrstr, target_str, start, end):
    if start > end:
        return None
    
    mid_index = (start+end)/2
    mid = arrstr[mid_index]
    
    if mid == target_str:
        return mid_index
    
    #for left
    left_end_index = mid_index
    while mid == "" and left_end_index > start:
        left_end_index -= 1
        mid = arrstr[left_end_index]
        if mid == target_str:
            return left_end_index
        
    if left_end_index >= start and target_str < mid:
        return bin_search(arrstr, target_str,start, left_end_index-1)
    
    #for right
    right_start_index = mid_index
    mid = arrstr[mid_index]
    while mid == "" and right_start_index < end:
        right_start_index += 1
        mid = arrstr[right_start_index]
        if mid == target_str:
            return right_start_index
        
    if right_start_index <= end and target_str > mid:
        return bin_search(arrstr, target_str, right_start_index+1, end)
    
    return None
        
        
def main_bin_search_string():
    strarr = ["at", "", "", "", "ball", "", "", "car","","","dad","",""]
    
    print bin_search(strarr, "at", 0, len(strarr)-1)
        
    
 




"""
11.6 Given an MxN matrix in which each row and each column is sorted in ascending
order, write a method to find an element.
"""
def search_matrix( mat, val, rs, re, cs, ce, result):
    if rs>re or cs>ce:
        return None
    
    
    mid_r = (rs+re)/2
    mid_c = (cs+ce)/2
    mid = mat[mid_r][mid_c]
    if mid == val:
        result.append((mid_r,mid_c))
        search_matrix( mat, val, rs, mid_r, mid_c+1, ce , result) #upper-right
        search_matrix( mat, val, mid_r+1, re, cs, mid_c , result) #lower-left
        
    
    elif val > mid:
        search_matrix( mat, val, rs, mid_r, mid_c+1, ce , result) #upper-right
        search_matrix( mat, val, mid_r+1, re, cs, mid_c , result) #lower-left
        search_matrix( mat, val, mid_r+1, re, mid_c+1, ce,result) # lower-right
    else:
        search_matrix( mat, val, rs, mid_r-1, mid_c, ce , result) #upper-right
        search_matrix( mat, val, mid_r, re, cs, mid_c-1 , result) #lower-left
        search_matrix( mat, val, rs, mid_r-1, cs, mid_c-1,result) #upper-left
        
        
    
def main_search_matrix():
    import numpy as np
    
    mat = np.zeros((4,4))
    
    mat = [
        [1,2,3,4],
        [2,3,4,5],
        [3,4,5,6],
        [4,7,8,9]
        ]
    
    print mat
    result = []
    search_matrix( mat, 7, 0, 3, 0, 3,result)
    print result
    
    
    
    
    
    



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


if __name__ == "__main__":
#     main_bubble_sort()
#     main_merge_sort()
#     main_quick_sort()
#     main_radix_sort()
#     main_radix_sort_msd()
#     main_merge_sorted_array()
#     main_sort_anagram_strings()
#     main_bin_search_string()
    main_search_matrix()
    
    print "\nDone!"