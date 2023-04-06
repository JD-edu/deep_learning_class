import numpy as np
import cv2


img = np.zeros((320, 240, 3), np.uint8)
cv2.putText(img , 'Conner Jeong', (100, 100) , cv2.FONT_HERSHEY_SIMPLEX, 5, (102,255,255))
cv2.putText(img , 'JD Edu', (50, 100) , cv2.FONT_HERSHEY_SIMPLEX, 5, (255,204,51))
cv2.imshow('my win',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
