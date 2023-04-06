import cv2
import numpy as np

cap = cv2.VideoCapture('car_video.avi')

while (cap.isOpened()):
  ret,img = cap.read()
  img_cvt = cv2.cvtColor( img, cv2.COLOR_BGR2HSV)
  img_mask = cv2.inRange( img_cvt,
      (np.array([ 140, 50, 50])), (np.array([ 180, 255, 255])))
  img_canny = cv2.Canny(img, 100, 100)
  cv2.imshow('my win',img_canny)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
    
