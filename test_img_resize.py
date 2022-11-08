import cv2
import numpy as np

print("Package Imported")

img = cv2.imread("Resources/airplane.png")

print(img.shape)

imgResize = cv2.resize(img, (500, 500))

cv2.imshow("Image", img)
cv2.imshow("Image Resized", imgResize)

cv2.waitKey(0)