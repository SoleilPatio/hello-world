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
p >? 3p^2 - 2p^3
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
THRESHOLD = 0.5
import math
class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set(self,x , y):
        self.x = x
        self.y = y
        
class line(object):
    def __init__(self, p1, p2):
        if abs(p2.x - p1.x) >  THRESHOLD:
            self.slope = (p2.y - p1.y) / (p2.x - p1.x)
            self.intercept = p1.y - self.slope * p1.x
        else:
            self.slope = None #slop == None means vertical line
            self.intercept = p1.x
            
    def __cmp__(self, other):
        
        if self.slope != None and other.slope != None:
#             print "cmp:slope(%f,%f) intercept(%f,%f)"%(self.slope,other.slope,self.intercept,other.intercept )
            if (abs(self.slope - other.slope) < THRESHOLD) and (abs(self.intercept - other.intercept) < THRESHOLD):
                return 0
            else:
                return -1
        elif self.slope == None and other.slope == None:
#             print "cmp:slope(None,None) intercept(%f,%f)"%(self.intercept,other.intercept )
            if (abs(self.intercept - other.intercept) < THRESHOLD):
                return 0
            else:
                return -1
        return -1
                
#     def __eq__(self, other):
#         print "i am eq",self.slope,other.slope,self.intercept ,other.intercept
#         if self.slope != None and other.slope != None:
#             if (abs(self.slope - other.slope) < THRESHOLD) and (abs(self.intercept - other.intercept) < THRESHOLD):
#                 return True
#             else:
#                 return False
#         elif self.slope == None and other.slope == None:
#             if (abs(self.intercept - other.intercept) < THRESHOLD):
#                 return True
#             else:
#                 return False
#         return False
        
            
class line_hash(object):
    def __init__(self):
        self.hash = {}
        
    def round_number(self, float_num):
        if float_num == None:
            return None
        q = int(float_num/THRESHOLD)
        return q*THRESHOLD
        
    def add_line_to_hash(self, line):
        key = self.round_number(line.slope)
        if key in self.hash:
            self.hash[key].append(line)
        else:
            self.hash[key] = [line]
        
    def count_identical_lines_by_slope(self, slope, line):
        key = self.round_number(slope)
        count = 0
        for l in self.hash.get(key,[]):
            cmp = line == l
            print "cmp=",cmp
            if cmp:
                count += 1
        return count
        
        
    def count_identical_lines(self,line):
        if line.slope == None:
            c1 = self.count_identical_lines_by_slope(line.slope, line)
            return c1
        else:
            c1= self.count_identical_lines_by_slope(line.slope-THRESHOLD, line)
            c2 = self.count_identical_lines_by_slope(line.slope, line)
            c3 = self.count_identical_lines_by_slope(line.slope+THRESHOLD, line)
        
        print c1,c2,c3,"=",c1+c2+c3
        return c1+c2+c3
                




def find_the_best_line(points):
    linstable = line_hash() #(slope:line list)
    
    max_count = 0
    best_line = None
    
    for i , p1 in enumerate(points):
        for j , p2 in enumerate(points[i+1:]):
            ll = line(p1,p2)
            linstable.add_line_to_hash(ll)
            count = linstable.count_identical_lines(ll)
            if (count > max_count):
                best_line = ll
                max_count = count
                
    return best_line, max_count
            


def main_find_best_line():
    POINT_COUNT = 50
    import numpy as np
    points = [point(0,0) for _ in range(POINT_COUNT)]
    randoms = np.random.randint(100, size = POINT_COUNT*2)
#     randoms = [10,10,20,20,30,30,40,40,50,50,60,60,70,70,80,80,90,90]
    print randoms
    for i in range(POINT_COUNT):
        points[i].set(float(randoms[i])/10, float(randoms[i+1])/10)
    
    for p in points:
        print p.x, p.y
    
    
    best_line, count = find_the_best_line(points)
    
    print "best_line.slope", best_line.slope, "best_line.intercept", best_line.intercept
    print "count", count
    
    import matplotlib.pyplot as plt
    
    plt.plot([points[i].x for i in range(POINT_COUNT) ], [points[i].y for i in range(POINT_COUNT)], "o" )
    
    if best_line.slope != None:
        x = [0,10]
        y = [best_line.slope*xi + best_line.intercept for xi in x ]
        
    else:
        x = [best_line.intercept, best_line.intercept]
        y = [0, 10]

    plt.plot(x, y)
    plt.show()
    
    
    
    
    


"""
7.7 Design an algorithm to find the kth number such that the only prime factors are
3,5, and 7.
"""




if __name__ == "__main__":
#     import timeit
#     
#     print timeit.timeit("main_gen_primes1()", setup="from __main__ import main_gen_primes1",number=1)
#     print timeit.timeit("main_gen_primes2()", setup="from __main__ import main_gen_primes2",number=1)
    
    main_find_best_line()



    
    print "Done!"
