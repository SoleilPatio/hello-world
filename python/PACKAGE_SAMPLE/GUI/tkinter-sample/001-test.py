# -*- coding: utf-8 -*-
from __future__ import print_function

try:
    # for Python2
    import Tkinter as tk
    import ttk #newer "themed widgets" that were added to Tk in 8.5.
except:
    # for Python3
    import tkinter as tk
    from tkinter import ttk


tk._test()
print( tk.Tcl().eval('info patchlevel') )
