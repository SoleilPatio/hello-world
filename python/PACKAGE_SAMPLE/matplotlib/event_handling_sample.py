import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

"""
plt.gcf() #get current figure (matplotlib.figure.Figure instance) ==> a windows
    How to change:
        plt.figure(1)
        plt.figure(2)
        
plt.gca() #get current axes (matplotlib.axes.Axes instance) ==> a axis
    How to change:
        plt.subplot(211)
        plt.subplot(212)
        

"""



def onclick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
    
def onkeypress(event):
    print('you pressed', event.key, event.xdata, event.ydata)

def onkeyrelease(event):
    print('you release', event.key, event.xdata, event.ydata)


if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(np.random.rand(10))
    
    cid1 = fig.canvas.mpl_connect('button_press_event', onclick)
    cid2 = fig.canvas.mpl_connect('key_press_event', onkeypress)
    cid3 = fig.canvas.mpl_connect('key_release_event', onkeyrelease)
    
    print cid1,cid2,cid3
    
    plt.show()
    
    
    print "\nDone!"