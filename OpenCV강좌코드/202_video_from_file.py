import cv2
import numpy as np
import time 


cap = cv2.VideoCapture('video.avi')
while (cap.isOpened()):
  ret,img = cap.read()
  cap.set(3, 640)
  cap.set(4, 480)
  img_cvt =  cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
  cv2.imshow('my win',img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
