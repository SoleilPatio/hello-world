# -*- coding: utf-8 -*-
import xlwings as xw

"""
Tutorial:
http://docs.xlwings.org/en/stable/udfs.html#udfs
"""
"""
[CLS]:
    create a excel project:
        > xlwings quickstart udf_sample_project

    hot key (in Excel):
        Alt + F8 : run macro => ImportPythonUDFs 
        Ctrl-Alt-F9 : refresh excel when python function change
        
"""
        

"""
[CLS]:必要decorator
"""
@xw.func
def double_sum(x, y):
    """Returns twice the sum of the two arguments"""
    return str(4 * (x + y))+u"中文"