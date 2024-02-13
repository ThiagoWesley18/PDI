import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('PDI/lena.jpg',0)

plt.hist(img.ravel(),256,[0,256])
plt.show()