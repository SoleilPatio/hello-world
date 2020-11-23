from wxglade_out import *

class MyHelloFrame(MyFrame):
    def __init__(self, *args, **kwds):
        super(MyHelloFrame, self).__init__(*args, **kwds)
        self.count = 1
        pass

    def OnLoad(self, event):  # wxGlade: MyFrame.<event_handler>
        print("I have implemented!")
        self.count += 1
        self.ui_message.write("Hello world! You press Load button!%d\n"%self.count)
        event.Skip() 


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyHelloFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()