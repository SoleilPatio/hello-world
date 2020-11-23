#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function



"""
-----------------------------------------------
Use below code to replace from ... import ...
can also use import_module("libPython.test_module")
-----------------------------------------------
"""
#...................................
# from test_module import TestMod
#...................................
import importlib
mymodule  = importlib.import_module("test_module")
print(mymodule )



if __name__ == '__main__':
    testobj = mymodule.TestMod()    #[CLS] TestMod can be a class name or function name
    testobj.Run()
    pass




