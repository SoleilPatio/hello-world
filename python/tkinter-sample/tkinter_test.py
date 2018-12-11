import Tkinter as tk

def demo1():
    print "[Run] demo1"
    root=tk.Tk()  #Create container, "root"
    root.mainloop()
    
def demo2():
    print "[Run] demo2"
    root=tk.Tk()  #Create container, "root"
    root.title("Tk GUI")
    
    label=tk.Label(root, text="Hello World!")   #Create "label" object
    label.pack() #Put "label" into container, "root"
    button=tk.Button(root, text="OK") #Create "button" object
    button.pack()     #Put "button" into container, "root"
    
    root.mainloop()
    
    
count = 10
label = None
I_AM_GLOBAL = "Hello Global!"
def demo3():
    print count
    print "[Run] demo3"
    global count
    global label
    print count
    
    count = count + 1
    
    
    root=tk.Tk()  #Create container, "root"
    root.title("Tk GUI")
    
    print type(label)
    label=tk.Label(root, text="Hello World!")   #Create "label" object
#     button=tk.Button(root, text="OK") #Create "button" object
    button=tk.Button(root, text="OK", command=clickOK)
    print type(label)
    """
    [CLS] use grid() instead of pack() to layout
    """
    label.grid(column=0,row=0)
    button.grid(column=1,row=0)
    
    root.mainloop()
    

def clickOK():
    
    global count
    global label
    print count
    count=count + 1
    label.configure(text="Click OK " + str(count) + " times")
    print I_AM_GLOBAL
    
    
    




if __name__ == '__main__':
#     demo1()
#     demo2() 
    demo3()
   
    
    pass