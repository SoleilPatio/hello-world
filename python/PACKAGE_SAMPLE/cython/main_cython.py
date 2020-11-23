"""
Actually import hello_cython.pyd(compiled python code).
Distutils or setuptools take care of this part.(don't know why)
"""
import hello_cython

if __name__ == '__main__':
    print hello_cython.normal_p_func(10)
    print hello_cython.normal_p_func2(10)
    print hello_cython.integrate_f(1,2,3)
    
#     print hello_cython.cdef_f(10) #cdef function cannot be called in python space ('module' object has no attribute 'cdef_f')
    print hello_cython.cpdef_f(10)
    
    pass