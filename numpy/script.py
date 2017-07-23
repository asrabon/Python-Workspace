import numpy
import cv2

img = cv2.imread("smallgray.png",0)
print(img)
for pixel in img.flat:
    print(pixel)
stacked = numpy.hstack((img,img))
print (stacked)
unstacked = numpy.hsplit(stacked,10)
print (unstacked)
