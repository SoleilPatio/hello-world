# -*- coding: utf-8 -*-
from __future__ import print_function

#[CLS] Windos OS: pip install -U wxPython
#[CLS] Linux OS:
#       lsb_release -a ==> check ubuntu version
#       pip install -U -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04 wxPython

# First things, first. Import the wxPython package.
import wx


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