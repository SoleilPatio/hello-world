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
"""

    
"""
9.2 Imagine a robot sitting on the upper left corner of an X by Y grid.The robot can
only move in two directions: right and down. How many possible paths are there
for the robot to go from (0,0) to (X,Y)?
FOLLOW UP
Imagine certain spots are "off limits," such that the robot cannot step on them.
Design an algorithm to find a path for the robot from the top left to the bottom
right.
"""


"""
9.3 A magic index in an array A[0.. .n-1] is defined to be an index such that A[i]
= i. Given a sorted array of distinct integers, write a method to find a magic
index, if one exists, in array A.
FOLLOW UP
What if the values are not distinct?
"""


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
    main_list_fibo()
    
    print "\nDone"
