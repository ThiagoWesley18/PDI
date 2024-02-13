import cv2
import numpy as np

# Filtro passa-baixa linear
# Suaviza o ruído

img = cv2.imread("PDI/Filtros/ruido.jpg")


img_out = cv2.GaussianBlur(img, (5,5), 0) # Filtro Gaussiano

cv2.imshow("ImagemEntrada",img)
cv2.imshow("ImagemFiltrada",img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()




