import numpy as np
import cv2

card_cascade = cv2.CascadeClassifier('Cascades/set_card_cascade_v3.xml')

img = cv2.imread('Test_Images/test1.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cards = card_cascade.detectMultiScale(gray_img, scaleFactor=1.04, minNeighbors=3, minSize=(30, 30))

for (x, y, w, h) in cards:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'card', (x+w, y+h), font, 0.5, (255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow('test', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
