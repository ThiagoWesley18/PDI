import cv2
import numpy as np

# Carrega a imagem em escala de cinza
img = cv2.imread('PDI/lena.jpg', 0)

# Calcula o alargamento de contraste quadrático
a = 0.1
b = 1
quadratic_image = np.uint8(a * (img ** 2) + b * img)

# Mostra a imagem original e a imagem com alargamento de contraste quadrático
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem com Alargamento de Contraste Quadrático', quadratic_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
