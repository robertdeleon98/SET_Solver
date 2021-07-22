import numpy as np
import cv2
import os

card_cascade = cv2.CascadeClassifier('Cascades/set_card_cascade_v3.xml')
dir = "Temp_Images"
img = cv2.imread('Test_Images/test6.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cards = card_cascade.detectMultiScale(gray_img, scaleFactor=1.04, minNeighbors=4, minSize=(30, 30))

for (x, y, w, h) in cards:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'card', (x+w, y+h), font, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
    roi_color = img[y:y + h, x:x + w]
    print("[INFO] Object found. Saving locally.")
    cv2.imwrite("Temp_Images/" + str(w) + str(h) + '_faces.jpg', roi_color)

cv2.imshow('test', img)
cv2.waitKey(0)

for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

cv2.destroyAllWindows()
