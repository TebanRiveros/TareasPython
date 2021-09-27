import cv2
import numpy as np

img = cv2.imread("Minecraft.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0) 

cv2.imshow("Imagen gris", imgGray)
cv2.waitKey(0)
cv2.imshow("Imagen azul", imgBlur)
cv2.waitKey(0)

kernel = np.ones((5,5), np.uint8)
imgCanny = cv2.Canny(img, 150, 200)
cv2.imshow("Bordes de la imagen ", imgCanny)
cv2.waitKey(0)

cv2.rectangle(img,(600, 330),(780,600),(255, 0, 0),2) 
cv2.imshow("Rectangulo", img)
cv2.waitKey(0)
