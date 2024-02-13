import cv2
import numpy as np

# Carrega a imagem em escala de cinza
img = cv2.imread('PDI/lena.jpg', cv2.IMREAD_GRAYSCALE)

# Calcula o alargamento de contraste logarítmico
a = 255 / np.log(1 + np.max(img))
log_image = a * (np.log(img + 1))

# Converte os valores de pixel para o intervalo [0, 255]
log_image = np.uint8(log_image)

# Mostra a imagem original e a imagem com alargamento de contraste logarítmico
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem com Alargamento de Contraste Logarítmico', log_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
