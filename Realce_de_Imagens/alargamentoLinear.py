import cv2
import numpy as np

img = cv2.imread('PDI/lena.jpg',0)
print(img)

min_val = np.min(img)
max_val = np.max(img)

out = (255/(max_val - min_val))*(img - min_val)
saida = np.uint8(out) # transforma uma matriz para uma matriz nao assinada(0-255)


cv2.imshow('Imagem',img)
cv2.imshow("ImagemSaida",saida)
cv2.waitKey(0)
cv2.destroyAllWindows()

