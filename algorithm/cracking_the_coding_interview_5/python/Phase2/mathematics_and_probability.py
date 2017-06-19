"""
generate prime numbers
sieve Of Eratosthenes
"""
def list_prime(max_number):
    import math
    ret = []
    
    for i in range(2, max_number + 1):
        b_found = False
        for j in ret:
            if j > math.sqrt(i):
                break
            if i%j == 0:
                b_found = True
                break
        if b_found == False:
            ret.append(i)
    return ret

def main_list_prime():
    print list_prime(1000)
        
        
def show_factors(num):
    import math
    ret = []
    prim_list = list_prime(int(math.sqrt(num)))
    print prim_list
    remain_num = num
    while remain_num:
        root = math.sqrt(remain_num)
        print "remain_num = ", remain_num,"root = ",root
        for i in prim_list:
            print "try i:", i
            if i > root:
                ret.append(remain_num)
                return ret
            else:
                if remain_num % i == 0:
                    ret.append(i)
                    remain_num = remain_num/i
                    break
    return ret
            
            
def main_show_factors():
    print show_factors(84)


"""
[REDO]
7.1 You have a basketball hoop and someone says that you can play one of two
games.
Game 1: You get one shot to make the hoop.
Game 2: You get three shots and you have to make two of three shots.
If p is the probability of making a particular shot, for which values of p should
you pick one game or the other
"""
"""
p >? 3p^2 - 2p^3
"""

"""math calculation"""

"""
7.2 There are three ants on different vertices of a triangle. What is the probability of
collision (between any two or all of them) if they start walking on the sides of the
triangle? Assume that each ant randomly picks a direction, with either direction
being equally likely to be chosen, and that they walk at the same speed.
Similarly, find the probability of collision with n ants on an n-vertex polygon
"""
"""math calculation"""

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
#     main_list_prime()
    main_show_factors()
    
    print "\nDone!"