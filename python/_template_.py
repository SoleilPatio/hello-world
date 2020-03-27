#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

try:
    # for Python2
    import Tkinter as tk
    import ttk  #newer "themed widgets" that were added to Tk in 8.5.
except:
    # for Python3
    import tkinter as tk
    from tkinter import ttk


if __name__ == '__main__':
    print("中文!Done!")