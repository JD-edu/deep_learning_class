import cv2
import numpy as np
import time

cap = cv2.VideoCapture('car_video.avi')
while (cap.isOpened()):
  ret,img = cap.read()
  cv2.imshow('my win',img)
  img_cvt =  cv2.cvtColor( img, cv2.COLOR_BGR2HSV)
  # Orange color
  # RGB: 215 109 85
  # Hue value: 6
  img_mask = cv2.inRange( img_cvt,
      (np.array([ 150, 50, 50])), (np.array([ 180, 255, 255])))
  cv2.imshow('gray',img_mask)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  time.sleep(0.1)
cap.release()
cv2.destroyAllWindows()
