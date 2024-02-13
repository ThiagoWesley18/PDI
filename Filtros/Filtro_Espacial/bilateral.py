import cv2
import numpy as np

# Filtro bilateral suaviza a imagem sem borrar as bordas
# Parametros:
#   - sigmaColor: desvio padrao do filtro gaussiano no dominio da intensidade (0 - 255). 
#     Quanto menor o valor, maior a definicao das bordas, borra menos.
#     Quanto maior o valor, mais borrado fica, mais parecido com o filtro gaussiano.
#   - sigmaSpace: desvio padrao do filtro gaussiano no dominio espacial (0 - 150).
#     Quanto menor o valor, mais borrado fica, mais parecido com o filtro gaussiano.
#     Quanto maior o valor, maior a definicao das bordas, borra menos.
#   - d: tamanho da vizinhanca usada no calculo do filtro (0 - 150).

img = cv2.imread("PDI/Filtros/ruido.jpg", 0)

# Parâmetros para o filtro bilateral
sigmaColor = 100
sigmaSpace = 100
d = 5

# Aplicar o filtro bilateral
img_out = cv2.bilateralFilter(img, d, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace)

# Salvar a imagem filtrada
cv2.imshow("ImagemEntrada",img)
cv2.imshow("ImagemFiltrada",img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()