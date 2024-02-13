import cv2
import numpy as np

# Filtro passa-baixa linear
# Suaviza o ruído

img = cv2.imread("PDI/Filtros/ruido.jpg")
#kernel = np.ones((5,5),np.float32)/25 # Filtro da media
#img_out = cv2.filter2D(img,-1,kernel) # faz a convolução

img_out = cv2.blur(img, (5,5)) # Filtro da media, faz a convolução com mascara 5x5

cv2.imshow("ImagemEntrada",img)
cv2.imshow("ImagemFiltrada",img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()