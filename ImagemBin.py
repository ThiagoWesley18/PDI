
import cv2

img= cv2.imread ('PDI/lena.jpg')

img= cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (0,0), fx=0.5,fy=0.5)

adp1= cv2.adaptiveThreshold (img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
adp2 = cv2.adaptiveThreshold (img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) 
lim, adp3= cv2.threshold (img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow("Raw Image", img)
cv2.imshow("LimiarAd MEAN", adp1)
cv2.imshow("LimiarAd GAUSS", adp2)
cv2.imshow("LimiarAd OTSU", adp3)
cv2.waitKey (0)
