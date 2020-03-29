# -*- coding: utf-8 -*-
from __future__ import print_function

# First things, first. Import the wxPython package.
import wx  #[CLS]: pip install -U wxPython


print("WX version = ", wx.version())    #[CLS] check wx version

# Next, create an application object.
app = wx.App()


# Then a frame.
frm = wx.Frame(None, title="Hello World")       #[CLS]: 一個Frame代表一個Window , 不需要跟App做連結（已自動連結)

frm2 = wx.Frame(None, title="Hello World 2")

# Show it.
frm.Show()

frm2.Show()

# Start the event loop.
app.MainLoop()