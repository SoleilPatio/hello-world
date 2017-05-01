
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
from _ast import Num
def insert(N, M, i , j):
    mask = (-1 & ~(1<<(j+1) -1)) | (1<<i-1)
    N = (N & mask ) | (M<<i)
    
    return bin(N)

def main_insert():
    print insert(int("10000000000",2), int("10011",2), 2, 6)
    
    

"""
5.2 Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately
in binary with at most 32 characters, print "ERROR."
"""
def float_to_bin(float_num):
    str_list = ["0","."]
    
    count = 1
    while count <= 32:
        quotation = int(float_num / 0.5)
        remainder = float_num % 0.5
        if quotation == 1:
            str_list.append("1")
        else:
            str_list.append("0")
            
        float_num = remainder*2
        count += 1
        
        if remainder == 0:
            break
        
    return "".join(str_list)
    
        
    
        
def main_float_to_bin():
    print float_to_bin(0.5)
    print float_to_bin(0.75)
    
    
    

"""
5.3 Given a positive integer, print the next smallest and the next largest number
that have the same number of 1 bits in their binary representation
"""
def next_smallest(num):
    n = num
    c0 = 0
    c1 = 0
    p = 0
    last = None
    while n:
        if n & 1:
            c1 += 1
            if last == 0: #found 0->1
                pass
            last = 1
        else:
            c0 += 1
            if last == 1: #found 1->0
                break
            last = 0
        n = n >> 1
        p += 1
        
    #we got p, c0, c1
    flip = 1<<p   #0->1 1's
    mask = ~((1<<(p+1)) -1)
    c1 = c1-1
    c0 = c0+1
    remain = (1<<c1) -1 #right most 1's
    
    ret = num & mask | flip | remain
    print bin(mask&0xFFFFFFFF)
    print bin(mask)
    print bin(flip)
    print bin(remain)
    
    print bin(num),"=",num
    print bin(ret),"=",ret
    return ret



def prev_largest(num):
    
    temp = num 
    c1 = 0
    p = 0
    last = None
    while temp:
        if temp & 1:
            
            if last == 0: #0->1 found
                break;
            c1 += 1
            last = 1
        else:
            last = 0
        
        temp = temp >> 1
        p += 1        
    
    
    #we got p, c1
    c1 = c1+1
    
    clear = ~((1 << (p+1)) - 1)
    remain1 = ((1<<c1)-1)<<(p-c1)
    
    ret = num & clear | remain1
    
    print bin(num),"=",num
    print bin(ret),"=",ret
    return ret
    
    
    
    
            
            
            
def main_same_1bit():
    next_smallest(13948)
    prev_largest(13948)
    


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

def convert_bit_count(A,B):
    a = A if A > 0 else A+0x10000
    b = B if B > 0 else B+0x10000
    
    print "A=", bin(a)
    print "B=", bin(b)
    count = 0
    while a or b:
        ba = a & 1
        bb = b & 1
        
        if ba != bb:
            count += 1
        
        a >>= 1
        b >>= 1
        
    return count

def main_convert():
    print convert_bit_count(-1,14)
        
        
        
        
        

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

def drawHorizontall_ine(bytes, width, x1, x2, y):
    start_byte = int((y*width+x1)/8)
    end_byte = int((y*width+x2)/8)

    full_start = start_byte if x1%8 == 0 else start_byte+1
    full_end = end_byte if x2%8 == 7 else end_byte-1
    
    if full_end > full_start:
        for i in range(full_start, full_end+1):
            bytes[i]=0xFF
            
    remainder = (y*width+x1)%8
    if remainder !=0:
        bytes[start_byte] = bytes[start_byte] | (1<<((7-remainder)+1))-1
        
    remainder = (y*width+x2)%8
    if remainder !=7:
        bytes[end_byte] = bytes[end_byte] | (0xFF & ~((1<<(7-remainder))-1))
        

def drawbyte(bytes,width, high):
    
    width_b = width/8
    for h in range(high):
        for wb in range(width/8):
            data = bytes[width_b*h + wb]
            for i in reversed(range(8)):
                if data & 1<<i == 0:
                    print ".",
                else:
                    print "O",
        print ""
        
def main_draw_line():
    import numpy as np
    width = 8*4
    hight = 8
    bytes = np.zeros(width*hight, dtype='b')
    
    drawbyte(bytes, width, hight)
    
    print "----------------------"
    drawHorizontall_ine(bytes, width, 10, 20, 3)
    drawbyte(bytes, width, hight)
    
    
        
        


if __name__ == "__main__":
#     main_insert()
#     main_float_to_bin()
#     main_same_1bit()
#     main_convert()
    main_draw_line()
    print "Done!"