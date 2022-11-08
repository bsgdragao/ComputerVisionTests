import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")
print(img.shape)

# # print(img)
# print('Largura em pixels: ', end='')
# print(img.shape[1]) #largura da imagem
# print('Altura em pixels: ', end='')
# print(img.shape[0]) #altura da imagem
# print('Qtde de canais: ', end='')
# print(img.shape[2])

# (b, g, r) = img[0, 0]
# print('O pixel (0, 0) tem as seguintes cores:')
# print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

width , height = 492,519

# for y in range(0, img.shape[0]):
#  for x in range(0, img.shape[1]):
#     img[y, x] = (255,0,0)
# cv2.imshow("Imagem modificada", img)

# for y in range(0, img.shape[0]): #percorre linhas
#  for x in range(0, img.shape[1]): #percorre colunas
#     img[y, x] = (x%256,y%256,x%256)
# cv2.imshow("Imagem modificada", img)
# cv2.waitKey(0)

# for y in range(0, img.shape[0], 1): #percorre as linhas
#  for x in range(0, img.shape[1], 1): #percorre as colunas
#     img[y, x] = (0,(x*y)%256,0)
# cv2.imshow("Imagem modificada", img)
# cv2.waitKey(0)

# for y in range(0, img.shape[0], 10): #percorre linhas
#     for x in range(0, img.shape[1], 10): #percorre colunas
#         img[y:y+5, x: x+5] = (0,255,255)
# cv2.imshow("Imagem modificada", img)
# cv2.waitKey(0)

pts1 = np.float32([[60,130],[260,150], [60,75],[492,519]])
pts2 = np.float32([[0,0],[width,0],[0,height], [width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutPut= cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutPut)

cv2.waitKey(0)