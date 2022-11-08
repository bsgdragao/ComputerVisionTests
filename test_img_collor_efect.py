import cv2
import numpy as np

print("Package Imported")

img = cv2.imread("Resources/airplane.png")
kernel = np.ones((5,5), np.uint8)

# cv2.imshow("Output", img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErode = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Erode Image", imgErode)

cv2.waitKey(0)
