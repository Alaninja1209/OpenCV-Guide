import cv2
import numpy as np

img = cv2.imread('MyPicGray.png') #Watch out for the repository

#Two parameters, the name of the window and the image itself
cv2.imshow('my image', img)
cv2.waitKey()

#Disposes all of the windows created by OpenCV
cv2.destroyAllWindows()
