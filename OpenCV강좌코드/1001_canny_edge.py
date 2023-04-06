import cv2


cap = cv2.VideoCapture('car_video.avi')
while (cap.isOpened()):
  ret,img = cap.read()
  cv2.imshow('my win',img)
  img_canny = cv2.Canny(img, 100, 100)
  cv2.imshow('canny',img_canny)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
