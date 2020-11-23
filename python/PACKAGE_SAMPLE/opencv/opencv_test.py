"""
[CLS]:pip install opencv-python
"""

import cv2
print cv2.__version__
from matplotlib import pyplot as plt



# Load an color image in grayscale
img = cv2.imread(r"D:\USERDATA\Pictures\10390029_859837767362637_2276634258536693955_n.jpg",0)


"""
[CLS]:Show with openCV
"""
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



"""
[CLS]:Use plt show , can be used in Jupyter without crash!
"""
plt.imshow(img,cmap='gray')
plt.show()




