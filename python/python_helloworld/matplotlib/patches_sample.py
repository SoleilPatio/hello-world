import matplotlib.pyplot as plt
import matplotlib.patches as patches

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



def RetangleTest():
    import numpy as np
    
    """
    [CLS]: get axis
    """
    ax = plt.subplot(111)
    
    
    coords = [np.random.randint(100, size=2) for _ in range(100) ]
    
    for coord in coords:
        """
        [CLS]: matplotlib color spec
             (r, g, b) or (r, g, b, a) where r,g,b,a in [0,1]
        """
        rect = patches.Rectangle(coord[0:2], 5, 2, angle=0 , color=np.random.rand(4) )
        """
        [CLS]: use axis to add patches
        """
        ax.add_patch(rect)

    
    plt.title('RetangleTest')
    plt.grid(True)
    
    plt.plot()
    plt.show()



if __name__ == "__main__":
    RetangleTest()
    
    print "\nDone!"