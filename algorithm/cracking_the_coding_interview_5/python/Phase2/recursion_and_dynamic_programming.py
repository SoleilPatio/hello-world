"""
ex1: recursive fibonacci w/ dynamic programming
ex2: iteration fibonacci
"""
def fibo(n):
    if n == 0 or n == 1:
        return 1
    
    if n in fibo.cache:
        return fibo.cache[n]
    
    if (n-1) in fibo.cache:
        fn_1 = fibo.cache[n-1]
    else:
        fn_1 = fibo(n-1)
        fibo.cache[n-1] = fn_1
    
    if (n-2) in fibo.cache:
        fn_2 = fibo.cache[n-2]
    else:
        fn_2 = fibo(n-2)
        fibo.cache[n-2] = fn_2
        
    num = fn_1 + fn_2
    fibo.cache[n] = num
    return num
    
fibo.cache = {}



def main_list_fibo():
    for i in range(1000):
        print fibo(i)
        



"""
9.1 A child is running up a staircase with n steps,and can hop either 1 step, 2 steps,
or 3 steps at a time. Implement a method to count how many possible ways the
child can run up
[CLS]:"step" parameter is no need
"""
def count_step(total,step=0):
    
    if total == 0:
        return 1
    elif total < 0:
        return 0
    
    if (total, step) in count_step.cached:
        return count_step.cached[(total, step)]
    
    if (total-1, 1) in count_step.cached:
        c1 = count_step.cached[(total-1, 1)]
    else:
        c1 = count_step(total-1, 1)
    
    if (total-2, 2) in count_step.cached:
        c2 = count_step.cached[(total-2, 2)]
    else:
        c2 = count_step(total-2, 2)
        
    if (total-3, 3) in count_step.cached:
        c3 = count_step.cached[(total-3, 3)]
    else:
        c3 = count_step(total-3, 3)
        
    count = c1 + c2 + c3
    count_step.cached[(total, step)] = count
    
    return count

count_step.cached = {}


def main_count_step():
    print count_step(10)

    
"""
9.2 Imagine a robot sitting on the upper left corner of an X by Y grid.The robot can
only move in two directions: right and down. How many possible paths are there
for the robot to go from (0,0) to (X,Y)?
FOLLOW UP
Imagine certain spots are "off limits," such that the robot cannot step on them.
Design an algorithm to find a path for the robot from the top left to the bottom
right.
"""
import numpy
def path_count(x,y):
    if x < 0 or y < 0:
        return 0
    if x == 0 and y == 0:
        return 1
    
    ret = path_count(x-1,y) + path_count(x,y-1)
    
    path_count.map[x][y] = ret
    
    return ret

X = 1
Y = 1
path_count.map = [[0 for _ in range(X+1)] for _ in range(X+1)]



def main_path_count():
    print path_count.map
    print path_count(X,X)
    print path_count.map
    
    


"""
9.3 A magic index in an array A[0.. .n-1] is defined to be an index such that A[i]
= i. Given a sorted array of distinct integers, write a method to find a magic
index, if one exists, in array A.
FOLLOW UP
What if the values are not distinct?
"""
def find_magic(a_list, start, end):
    if start > end:
        return None
    
    mid = (start+end) /2
    
    if mid == a_list[mid]:
        return mid
    elif mid > a_list[mid]:
        return find_magic(a_list, mid+1, end)
    else:
        return find_magic(a_list, start, mid-1)
    
    
def main_find_magic():
    a = [-1,-1,1,2,4,8,9,10,11,11,11,11]
    
    print find_magic(a, 0, len(a)-1)
    
    
    
    
    
    
    
    
    

"""
9.4 Write a method to return all subsets of a set.
"""


"""
9.5 Write a method to compute all permutations of a string.
"""


"""
9.6 Implement an algorithm to print all valid (e.g., properly opened and closed)
combinations of n-pairs of parentheses.
EXAMPLE
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()
"""



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
board so that none of them share the same row, column or diagonal. In this case,
"diagonal" means all diagonals, not just the two that bisect the board.
"""



"""
9.10 You have a stack of n boxes,with widths wi, heights hi, and depths di.The boxes
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
Expression:1^0|0|1
Desired result: false (0)
Output: 2ways. 1^((0|0)|1) and 1^(0|1(0|1)).
"""


if __name__ == "__main__":
#     main_list_fibo()
#     main_count_step()
#     main_path_count()
    main_find_magic()
    
    print "\nDone"
