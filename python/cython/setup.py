'''
'''
import sys
from Cython.Build import cythonize


if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    #Python 2.6
    """
    use distutils.core.setup in python 2.7 will cause "error: Unable to find vcvarsall.bat"
    """
    from distutils.core import setup #error: Unable to find vcvarsall.bat
    
    from distutils.extension import Extension
else:
    #Python 2.7
    from setuptools import setup
    from setuptools import Extension




setup(
#     ext_modules = cythonize("hello_cython.pyx")
    ext_modules = cythonize( [  Extension('hello_cython', ['hello_cython.pyx'] ) ] )
    )
