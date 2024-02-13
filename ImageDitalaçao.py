
import cv2
import numpy as np
img = cv2.imread('PDI/lena.jpg', 0)
kernel = np.ones((3,3), np.uint8)
 
img_dilation = cv2.dilate(img, kernel, iterations=1)
 
cv2.imshow('Input', img)
cv2.imshow('Dilation', img_dilation)
 
cv2.waitKey(0)
cv2.destroyAllWindows()