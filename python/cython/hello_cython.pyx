"""
http://docs.cython.org/en/latest/src/quickstart/cythonize.html

0. pip install Cython
1. hello_cython.pyx ==> source file
2. setup.py ==> cython makefile
    2-1: python setup.py build_ext --inplace
        a. hello_cython.so (unix)
        b. helloworld.pyd (windows)
        
3. import  hello_cython
    3-1: import will only find *.pyd(compiled file) instead of *.pyx (source file)
    3-2: Distutils or setuptools take care of this part
        
"""

print "hello cython!"


def normal_p_func( x ):
    return x ** 2 - x

def normal_p_func2( double x ):
    return x ** 2 - x

def integrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += normal_p_func2(a + i * dx)
    return s * dx


"""
cdef can not be called in python space
"""
cdef double cdef_f(double x) except? -2:
    return x ** 2 - x

"""
cpdef can be called in both python space and cython-space, because it create a wrapper
"""
cpdef double cpdef_f(double x) except? -2:
    return x ** 2 - x


