import cv2
import numpy as np



# Carrega a imagem
img = cv2.imread('PDI/lena.jpg', cv2.IMREAD_GRAYSCALE)

# Aplica o alargamento de contraste exponencial
# Normaliza a imagem para o intervalo [0, 1]
normalized_image = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

# Aplica o alargamento de contraste exponencial
a = 255 / np.log(1 + np.max(img))
stretched_image = a * np.exp(normalized_image ) - 1

# Normaliza a imagem resultante para o intervalo [0, 255]
saida = cv2.normalize(stretched_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)


# Salva a imagem resultante
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem Saida', saida )
cv2.waitKey(0)
cv2.destroyAllWindows()