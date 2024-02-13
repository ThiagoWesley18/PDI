import cv2
import numpy as np

# Filtro passa-baixa não linear
# Suaviza o ruído

img = cv2.imread("ruido.jpg")

# Filtro da mediana, usa uma mascara 5x5 e calcula a mediana dos valores, aa mascara precisa ser impar.
img_out = cv2.medianBlur(img, 5) 

cv2.imshow("ImagemEntrada",img)
cv2.imshow("ImagemFiltrada",img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()