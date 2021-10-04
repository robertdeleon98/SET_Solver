import numpy as np
import cv2
import os
import math

img = cv2.imread('Test_Images/test4.jpg')
test_cards = ["1-2_2-4.jpg", "132-223_24-443.jpg", "12-23_24-43.jpg"]
# format: x-y_w-h.jpg
for z in range(3):
    card = test_cards[z]
    i = 0
    x, y, w, h = '', '', '', ''

    while card[i] != '-':
        x += card[i]
        i += 1
    else:
        i += 1
        while card[i] != '_':
            y += card[i]
            i += 1
        else:
            i += 1
            while card[i] != '-':
                w += card[i]
                i += 1
            else:
                i += 1
                while card[i] != '.':
                    h += card[i]
                    i += 1
                else:
                    pass
    x = int(x)
    y = int(y)
    w = int(w)
    h = int(h)

    img = cv2.imread('Test_Images/test4.jpg')
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


cv2.imshow('test', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
