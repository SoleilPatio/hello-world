"""
ex1: recursive fibonacci w/ dynamic programming
ex2: iteration fibonacci
"""
from multiprocessing import Queue
def fibonacci(nth):
    if nth == 1:
        return 0
    elif nth == 2:
        return 1
    
    if nth in fibonacci.map: 
        return fibonacci.map[nth]
    fibonacci.map[nth] = fibonacci(nth-1) + fibonacci(nth-2)
    return fibonacci.map[nth]

fibonacci.map = {}    


def fibonacci_it(nth):
    if nth == 1:
        return 0
    elif nth == 2:
        return 1
    
    last1 = 0
    last2 = 1
    
    for i in range(3,nth+1):
        sum = last1+last2
        last1 = last2
        last2 = sum
        
    return sum
    
    
    


def main_fibonacci():
    for i in range(1,50):
        print fibonacci(i),
        
    print ""
    
    for i in range(1,50):
        print fibonacci_it(i),
        
    print ""

"""
9.1 A child is running up a staircase with n steps,and can hop either 1 step, 2 steps,
or 3 steps at a time. Implement a method to count how many possible ways the
child can run up
"""

def count_possible_step(next_step, total_step_count, target_step_count, path_list):
    
    current_total = next_step + total_step_count
    path = list(path_list)
    path.append(next_step)
    if current_total == target_step_count:
        print path
        return 1
    elif current_total > target_step_count:
        return 0
    else:
        s1 = count_possible_step(1, current_total, target_step_count,path)
        s2 = count_possible_step(2, current_total, target_step_count,path)
        s3 = count_possible_step(3, current_total, target_step_count,path)
        return s1+s2+s3


def main_count_possible_step():
    print count_possible_step(0, 0, 10, [])
    
def count_possible_step_dynamic(next_step, total_step_count, target_step_count, path_list, map):
    
    current_total = next_step + total_step_count
    path = list(path_list)
    path.append(next_step)
    if current_total == target_step_count:
        print path
        return 1
    elif current_total > target_step_count:
        return 0
    else:
        if current_total in map:
            return map[current_total]
        else:
            s1 = count_possible_step_dynamic(1, current_total, target_step_count,path, map)
            s2 = count_possible_step_dynamic(2, current_total, target_step_count,path, map)
            s3 = count_possible_step_dynamic(3, current_total, target_step_count,path, map)
            map[current_total] = s1+s2+s3
            return map[current_total]


def main_count_possible_step_dynamic():
    map = {}
    print count_possible_step_dynamic(0, 0, 10, [], map)
    print map
    

def main_count_possible_step_compare():
    import timeit
    t1 = timeit.timeit("main_count_possible_step()",setup="from __main__ import main_count_possible_step",number=10)
    t2 = timeit.timeit("main_count_possible_step_dynamic()",setup="from __main__ import main_count_possible_step_dynamic",number=10)
    print t1,t2
    
    
    
"""
9.2 Imagine a robot sitting on the upper left corner of an X by Y grid.The robot can
only move in two directions: right and down. How many possible paths are there
for the robot to go from (0,0) to (X,Y)?
FOLLOW UP
Imagine certain spots are "off limits," such that the robot cannot step on them.
Design an algorithm to find a path for the robot from the top left to the bottom
right.
"""
def possible_path(x,y):
    if x == 0:
        return 1
    if y == 0:
        return 1
    
    if (x,y) in possible_path.map:
        return possible_path.map[(x,y)]
    possible_path.map[(x,y)] = possible_path(x-1, y) + possible_path(x, y-1)
    return possible_path.map[(x,y)] 

possible_path.map = {
    }
    

def main_possible_path():
    X=10
    Y=10
    
    for i in range(0, X+1):
        for j in range(0, Y+1):
            print "%6d"%possible_path(i,j),
        print ""


"""
9.3 A magic index in an array A[0.. .n-1] is defined to be an index such that A[i]
= i. Given a sorted array of distinct integers, write a method to find a magic
index, if one exists, in array A.
FOLLOW UP
What if the values are not distinct?
"""
def find_magic(start, end, A):
    print start,end
    if end < start:
        return 0

    mid = (start+end)/2
    
    if A[mid] == mid:
        return mid
    elif A[mid] > mid:
        return find_magic(start, mid-1, A)
    else:
        return find_magic(mid+1, end, A)
    
def find_magic2(start, end, A):
    print start,end
    if end < start:
        return 0

    mid = (start+end)/2
    
    if A[mid] == mid:
        return mid
    elif A[mid] > mid:
        left = find_magic(start, mid-1, A)
        if left != 0:
            return left
        else:
            return find_magic(A[mid], end, A)
            
    else:
        right = find_magic(mid+1, end, A)
        if right != 0:
            return right
        else:
            return find_magic(start, A[mid], A)
        
        
    
def main_find_magic():
    A = [None, -20,-1,1,2,3,5,7,9,12,13]

    print find_magic(1,10,A)
    
    A2 = [None, -5,2,2,2,3,4,7,9,12,13]
#     A2 = [None, -5,2,2,2,3,4,8,9,12,13]
    
    print find_magic2(1,10,A2)

"""
9.4 Write a method to return all subsets of a set.
"""
def all_subset(index, parent_set, super_set, result_subsets):
    if index >= len(super_set):
        return
     
    my_set = list(parent_set)
    
    #not select
    all_subset(index+1, my_set, super_set, result_subsets)
    
    #selected
    my_set.append(super_set[index])
    result_subsets.append(my_set)
    all_subset(index+1, my_set, super_set, result_subsets)
   
        
        
    
def main_all_subset():
    result = []
    super_set = [0,1,2,3,4,5]
    all_subset(0, [],super_set, result )
    
    for set in result:
        print set
    print "len =", len(result)
    
    
    


"""
9.5 Write a method to compute all permutations of a string.
"""
def permutate_string(instr):
    import collections
    level_queue = collections.deque()
    
    level_queue.append(([],list(instr)))
    
    count = 1
    while level_queue:
        path, remain = level_queue.popleft()
        
        if remain == []:
            print count,":","".join(path)
            count +=1
        
        for i, c in enumerate(remain):
            new_remain = list(remain)
            del new_remain[i]
            new_path = list(path)
            new_path.append(c)
            level_queue.append((new_path, new_remain))
            

def permutate_string_recursive(instr):
    str_list = list(instr)
    
    if len(str_list) == 0:
        return [[]]


    c = str_list.pop() #the right most character
    new_str = "".join(str_list)
    per_list = permutate_string_recursive(new_str)
    
    ret_list = []
    for p in per_list:
        for i in range(len(p)+1):
            new_p = list(p)
            new_p.insert(i,c)
            ret_list.append(new_p)
            
    return ret_list
        
    
    
    
    
            
def main_permutate_str():
#     permutate_string("Clouds")
    ret_list = permutate_string_recursive("Clouds")
    
    for i,p in enumerate(ret_list):
        print i+1,"".join(p)
    
    
        
    





"""
9.6 Implement an algorithm to print all valid (e.g., properly opened and closed)
combinations of n-pairs of parentheses.
EXAMPLE
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

def parentheses(n):
    import collections
    remain_r = n
    remain_l = n
    
    queue = collections.deque()
    
    remain_l = remain_l-1
    queue.append( (remain_r, remain_l, ['(']))
    
    resutl_list = []
    while queue:
        r, l, str_list = queue.popleft()
        
        
        if l > 0:
            new_list = list(str_list)
            new_list.append('(')
            queue.append( (r, l-1, new_list ))
            
        if r > 0 and r > l:
            new_list = list(str_list)
            new_list.append(')')
            queue.append( (r-1, l, new_list))
        
        if r == 0 and l == 0:
            new_list = list(str_list)
            resutl_list.append(new_list)
            
    for i,l in enumerate(resutl_list):
        print i,":","".join(l)
        
            
    
def main_parentheses():
    parentheses(3)
        
    





"""
9.7 Implement the "paint fill" function that one might see on many image editing
programs. That is, given a screen (represented by a two-dimensional array of
colors), a point, and a new color, fill in the surrounding area until the color
changes from the original color.
"""

""""
9.8 Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5
cents) and pennies (1cent), write code to calculate the number of ways of representing n cents.
"""

"""
9.9 Write an algorithm to print all ways of arranging eight queens on an 8x8 chess
board sothat none of them share the same row, column or diagonal. In this case,
"diagonal" means all diagonals, not just the two that bisect the board.
"""

"""
9.10 You have a stack of n boxes,with widths w., heights hir and depths drTheboxes
cannot be rotated and can only be stacked on top of one another if each box
in the stack is strictly larger than the box above it in width, height, and depth.
Implement a method to build the tallest stack possible, where the height of a
stack is the sum of the heights of each box
"""

"""
9.11 Given a boolean expression consisting of the symbols 0,1, &, |, and A, and a
desired boolean result value result,implement afunction to count the number
of ways of parenthesizing the expressionsuch that it evaluatesto result.
EXAMPLE
Expression:1A01011
Desired result: false (0)
Output: 2ways. 1A((010) 11) and1A(91 (011)).
"""



if __name__ == "__main__":
#     main_count_possible_step_compare()
#     main_fibonacci()
#     main_possible_path()
#     main_find_magic()
#     main_all_subset()
#     main_permutate_str()
    main_parentheses()
    
    
    print "Done"