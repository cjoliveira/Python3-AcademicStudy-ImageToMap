import cv2
import numpy as np
import math 

img = cv2.imread('img.jpeg', 0) # Lê a imagem em escala preto e branco
img = cv2.resize(img, (400,400), interpolation = cv2.INTER_AREA) # Converte a imagem para dimensao dada
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # Transforma a imagem em preto(0) e branco(255)

contours, hierarchy = cv2.findContours(image=bw_img, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE) # Encontra os pontos de contorno, index: 0

# Cria o Numpy Array com os pontos de contorno no formato necessário para o Algoritmo
contoursPointsList = []
for i in range(len(contours)):
    for point in contours[i]:
        contoursPointsList.append(point[0].tolist())

contoursPointsArray = np.array(contoursPointsList)
print(contoursPointsArray)
cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()