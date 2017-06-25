
"""
5.1 You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write
a method to insert M into N such that M starts at bit j and ends at bit i. You can
assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You
would not, for example, have j = 3 and i = 2, because M could not fully fit
between bit 3 and bit 2.
EXAMPLE
Input: N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100
"""

def insert(N, M, i, j):
    ret = ( 0xFFFFFFFF & ~((1 << (j+1))-1) ) | ((1<<(i+1))-1)
    print bin(ret)
    
    ret = N & ret
    print bin(ret)
    
    ret = ret | (M << i)
    print bin(ret)
    
    return ret
    
def main_insert():
    ret = insert( 0b10000000000, 0b10011, 2, 6)
    
    print bin(ret)
    


"""
5.2 Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately
in binary with at most 32 characters, print "ERROR."
"""
def show_binary(realnum):
    
    rep = []
    for i in range(1,33):
        div = (1.0/2)**i
        if realnum >= div:
            rep.append("1")
            realnum -= div
        else:
            rep.append("0")
        if realnum <= 0:
            break
    
    return "b0." + "".join(rep)


def main_show_binary():
    print show_binary(0.75)
            
            

        
        
    


"""
5.3 Given a positive integer, print the next smallest and the next largest number
that have the same number of 1 bits in their binary representation
"""
def find_next_smallest(n):
    bin_n_str = bin(n)
    print bin_n_str
    
    first_1_0_index = -1
    trailing_0_count = 0
    
    temp = n
    
    b_found_1 = False
    
    for i in range(64):
        if temp & (1<<i) != 0:
            b_found_1 = True
        else:
            if b_found_1 == False:
                trailing_0_count += 1
            else:
                first_1_0_index = i
                break
            
    if first_1_0_index == -1:
        print "Error"
        return None
    
    print first_1_0_index
    print trailing_0_count
    
    ret = n
    
    first_part = n >> (first_1_0_index)
    second_part = n & (1<<first_1_0_index-1)-1
    
    print bin(first_part)
    print bin(second_part)
    
    f_part = ( (first_part|1) <<  (first_1_0_index) )
    s_part = second_part >> trailing_0_count
    
    print bin(f_part)
    print bin(s_part)
    
    ret = f_part | s_part
    
    print ret
    print bin(ret)
    
    
                
            
        
    
    
    
    
    
    
def main_find_next():
    n = 13948
    find_next_smallest(n)


"""
5.4 Explain what the following code does: ((n & (n-1)) == 0).
"""

"""
5.5 Write a function to determine the number of bits required to convert integer A
to integer B.
EXAMPLE
Input: 31,14
Output: 2
"""
def count_diff_bit(a,b):
    c=a^b
    
    print bin(a)
    print bin(b)
    print bin(c)
    
    
    count = 0
    while c:
        
        print bin(c)
        if (c & 1) == 1:
            count += 1
            print "count", count
        c = (c >> 1)
    
    return count

def main_count_diff_bit():
    print count_diff_bit(31,14)
    
            
        
   
        

"""
5.6 Write a program to swap odd and even bits in an integer with as few instructions
as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and
soon).
"""

"""
5.7 An array A contains all the integers from 0 to n, except for one number which is
missing. In this problem, we cannot access an entire integer in A with a single
operation. The elements of A are represented in binary, and the only operation
we can use to access them is "fetch the jth bit of A[i]," which takes constant
time. Write code to find the missing integer. Can you do it in 0(n) time?
"""

"""
5.8 A monochrome screen is stored as a single array of bytes, allowing eight consecutive
pixels to be stored in one byte.The screen has width w, where w is divisible
by 8 (that is, no byte will be split across rows).The height of the screen, of course,
can be derived from the length of the array and the width. Implement a function
drawHorizontall_ine(byte[] screen, int width, int x1, int x2,
int y) which draws a horizontal line from (x1, y)to(x2, y).
"""


if __name__ == "__main__":
#     main_insert()
#     main_show_binary()
#     main_find_next()
    main_count_diff_bit()
    
    print "\nDone"
