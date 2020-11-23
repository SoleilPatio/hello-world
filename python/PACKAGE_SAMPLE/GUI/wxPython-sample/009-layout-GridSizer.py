
# https://www.tutorialspoint.com/wxpython/wx_gridsizer.htm

import wx
  
class Example(wx.Frame): 
   
   def __init__(self, parent, title): 
      super(Example, self).__init__(parent, title = title,size = (300,200)) 
             
      self.InitUI() 
      self.Centre() 
      self.Show()      
         
   def InitUI(self): 
	
      p = wx.Panel(self) 
         
      gs = wx.GridSizer(4, 4, 5, 5) 
		
      for i in range(1,17): 
         btn = "Btn"+str(i) 
         gs.Add(wx.Button(p,label = btn),0,wx.EXPAND) 

         p.SetSizer(gs)  
   
app = wx.App() 
Example(None, title = 'Grid demo') 
app.MainLoop()