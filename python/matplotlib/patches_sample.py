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

def RectangleTest2():
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import numpy as np
    
    """
    [CLS]: get axis
    """
    ax = plt.subplot(111)
    
    
    coords = [np.random.randint(100, size=2) for _ in range(100) ]
    
    rect1 = patches.Rectangle([2,2], 5, 5, angle=0 , color="red", label="name1" , alpha=0.5)
    
    ax.text(2+5./2, 2+5./2, 'red',
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=11, color='black')
#         transform=ax.transAxes)
    
    rect2 = patches.Rectangle([0,0], 3, 3, angle=0 , color="blue", label="name2", alpha=0.5 )
    
    ax.text(0+3./2, 0+3./2, 'blue',
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=11, color='black')
#         transform=ax.transAxes)
    
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    
    
#     for coord in coords:
#         """
#         [CLS]: matplotlib color spec
#              (r, g, b) or (r, g, b, a) where r,g,b,a in [0,1]
#         """
#         rect = patches.Rectangle(coord[0:2], 5, 2, angle=0 , color=np.random.rand(4) )
#         """
#         [CLS]: use axis to add patches
#         """
#         ax.add_patch(rect)

    
    plt.title('RetangleTest')
    plt.grid(True)
    
#     ax.set_axis_off()
    
    plt.plot()
    plt.show()

    


if __name__ == "__main__":
#     RetangleTest()
    RectangleTest2()
    
    print "\nDone!"