import cv2
import numpy as np


img_file = cv2.imread("lena.jpg",cv2.IMREAD_COLOR)
img_gray = cv2.imread("lena.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow('color',img_file)
cv2.imshow('gray',img_gray)
cv2.waitKey(2000)
cv2.destroyAllWindows()
