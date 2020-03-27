# -*- coding: utf-8 -*-
from __future__ import print_function

# First things, first. Import the wxPython package.
import wx  #[CLS]: pip install -U wxPython

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()