import cv2
import numpy
import os

img = cv2.imread('OpenCV/MyPic.png')

#Tuple describing shape of image (height, width, channels -> If is BGR)
print(img.shape)

#Number of elements in the array
print(img.size)

#Data type of array's elements, 8 bit-per-channel 
print(img.dtype)

#image[0, 0, 0] or image[0, 0]. First index "y" coordinates, second index "x" coordinates, third index color channel

#Creating an array of 120,000 random bytes
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

#Convert an array to make a 400x300 grayscale image
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('RandomGray.png',grayImage)

#Convert an array to make a 400x300 colour image
bgrImage = flatNumpyArray.reshape(100, 400 , 3)
cv2.imwrite('RandomColor.png', bgrImage)
