def my_gen_primes( max ):
    import math
    prime_list = [2]
    for num in range(3, max+1, 2):
        
        factor_found = False
        for p in prime_list:
            if p > math.sqrt(num):
                break
            if num%p == 0:
                factor_found = True
                break
            
        if factor_found == False:
            prime_list.append(num)
    return prime_list

def sieveOfEratosthenes(max):
    import numpy as np
    import math
    flag = np.ones(max+1,dtype="b")
    flag[0] = False
    flag[1] = False
    
    num = 2
    sqrt_max = int(math.sqrt(max))
    while num < sqrt_max:
        #mask
        for i in range(num*num, max+1, num):
            flag[i] = False
        
        #next num
        for i in range(num+1, max+1):
            num = i
            if flag[i] == True:
                break
            
    #return list
    ret_list = []
    for i, data in enumerate(flag):
        if data:
            ret_list.append(i)
            
    return ret_list
    
    
    
    

def main_gen_primes1():
    print my_gen_primes(1000000)
def main_gen_primes2():
    print sieveOfEratosthenes(1000000)


"""
7.1 You have a basketball hoop and someone says that you can play one of two
games.
Game 1: You get one shot to make the hoop.
Game 2: You get three shots and you have to make two of three shots.
If p is the probability of making a particular shot, for which values of p should
you pick one game or the other
"""

"""
7.2 There are three ants on different vertices of a triangle. What is the probability of
collision (between any two or all of them) if they start walking on the sides of the
triangle? Assume that each ant randomly picks a direction, with either direction
being equally likely to be chosen, and that they walk at the same speed.
Similarly, find the probability of collision with n ants on an n-vertex polygon
"""

"""
7.3 Given two lines on a Cartesian plane, determine whether the two lines would
intersect.
"""

"""
7.4 Write methods to implement the multiply, subtract, and divide operations for
integers. Use only the add operator.
"""

"""
7.5 Given two squares on a two-dimensional plane, find a line that would cut these
two squares in half. Assume that the top and the bottom sides of the square run
parallel to the x-axis.
"""

"""
7.6 Given a two-dimensional graph with points on it, find a line which passes the
most number of points.
"""

"""
7.7 Design an algorithm to find the kth number such that the only prime factors are
3,5, and 7.
"""




if __name__ == "__main__":
    import timeit
    
    print timeit.timeit("main_gen_primes1()", setup="from __main__ import main_gen_primes1",number=1)
    print timeit.timeit("main_gen_primes2()", setup="from __main__ import main_gen_primes2",number=1)
    
    print "Done!"
