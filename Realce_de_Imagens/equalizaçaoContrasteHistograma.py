import cv2

# Carrega a imagem em escala de cinza
img = cv2.imread('PDI/lena.jpg', cv2.IMREAD_GRAYSCALE)

# Aplica a equalização de contraste por histograma
equalized_image = cv2.equalizeHist(img)

# Mostra a imagem original e a imagem com equalização de contraste por histograma
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem com Equalização de Contraste por Histograma', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
