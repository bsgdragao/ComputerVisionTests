import cv2
import numpy as np

print("Package Imported")

img = cv2.imread("Resources/airplane.png")

print(img.shape)

imgCropped = img[0:100, 0:150]

cv2.imshow("Image", img)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)