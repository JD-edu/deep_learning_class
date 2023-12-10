import cv2
from tensorflow.keras.models import load_model
import numpy as np
class_labels = ["cans", "cups", "pets"]
model = load_model("vgg_cans.h5")

#img = cv2.imread("./images/cans/cans(1).jpg")
img = cv2.imread("cans.jpg")
img_scaled = cv2.resize(img, (64, 64), interpolation=cv2.INTER_AREA)
data = img_scaled
data = data.astype("float")/255.0
X= np.asarray([data])
s = model(X, training=False)
print(s)
