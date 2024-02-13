import cv2
import numpy as np

# Filtro passa-alta
# Realça as bordas

img = cv2.imread("PDI/lena.jpg", 0) # lê em tons de cinza


img_out = cv2.Canny(img, 70, 150) # Filtro Gaussiano

cv2.imshow("ImagemEntrada",img)
cv2.imshow("ImagemFiltrada",img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()