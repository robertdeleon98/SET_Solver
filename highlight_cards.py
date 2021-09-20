import numpy as np
import cv2
import os
import math

img = cv2.imread('Test_Images/test4.jpg')


# format: x-y_w-h.jpg
test_card = "9-5_219-146.jpg"
print(len(test_card))

first_value_flag = True
i = 0
x, y, w, h = '', '', '', ''


while test_card[i] != '_':
    while first_value_flag:
        if test_card[i] != '-':
            x = x + test_card[i]
            i += 1
        else:
            first_value_flag = False

    y = y + test_card[i]
    i += 1


print(x, y)
