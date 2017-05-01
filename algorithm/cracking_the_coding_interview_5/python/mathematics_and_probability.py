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


if __name__ == "__main__":
    import timeit
    
    print timeit.timeit("main_gen_primes1()", setup="from __main__ import main_gen_primes1",number=1)
    print timeit.timeit("main_gen_primes2()", setup="from __main__ import main_gen_primes2",number=1)
    
    print "Done!"
