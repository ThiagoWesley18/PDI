import cv2


# Carregar a imagem 
# parametros:
# 0 - carrega a imagem em escala de cinza
# 1 - carrega a imagem no padrão RGB
img = cv2.imread("PDI/lena.jpg", 1) 
print("Bem vindo ao Python com OPenCV\n")

# Redimensiona a imagem em 50%
img = cv2.resize(img, (0,0), fx=0.5 , fy=0.5)

# Imagem em escala de cinza
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



cv2.imshow('Imagem',img)# mostra a imagem em uma janela

cv2.waitKey(0) # fecha a imagem depois do tempo definido no parametro (ms), caso nao seja defenido 
               # o parametro (0), então a jenela fecha ao apertar uma tecla.

cv2.destroyAllWindows() # Fecha todas as janelas ao mesmo tempo
