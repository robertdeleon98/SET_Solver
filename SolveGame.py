'''
SET Rules
They all have the same color or have three different colors.
They all have the same shading or have three different shadings.
They all have the same shape or have three different shapes.
They all have the same number or have three different numbers.
'''


# import numpy as np
# import pandas as pd
# import cv2
# import os
# from random import shuffle
# from tqdm import tqdm
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import imread, imshow, subplots, show


class Card:
    def __init__(self, color, shading, shape, number):
        self.color = color
        self.shading = shading
        self.shape = shape
        self.number = number


# card1 = Card('', '', '', '')
# filename = "p-e-d-2.PNG"
# print(len(filename))
# i = 0
# while filename[i] != '.':
#     if filename[i] == 'r':
#         card1.color = 'red'
#     elif filename[i] == 'g':
#         card1.color = 'green'
#     elif filename[i] == 'p':
#         card1.color = 'purple'
#     elif filename[i] == 'f':
#         card1.shading = 'full'
#     elif filename[i] == 'l':
#         card1.shading = 'lines'
#     elif filename[i] == 'e':
#         card1.shading = 'empty'
#     elif filename[i] == 'o':
#         card1.shape = 'oval'
#     elif filename[i] == 'd':
#         card1.shape = 'diamond'
#     elif filename[i] == 's':
#         card1.shape = 'squiggly'
#     elif filename[i] == '1':
#         card1.number = 'one'
#     elif filename[i] == '2':
#         card1.number = 'two'
#     elif filename[i] == '3':
#         card1.number = 'three'
#     i += 1
#
# print(card1.color, card1.shading, card1.shape, card1.number)


# number = ['one', 'two', 'three']
# shape = ['oval', 'diamond', 'squiggly']
# shading = ['full', 'lines', 'empty']
# color = ['red', 'green', 'purple']
#
#
#
#
# image = imread('image-data/positive-images/r-f-s-2.PNG')
# images = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# imshow(images[0])
# show()

'''
read image name and extract features from image file name
if color = red
    then card.color=red
if shape = squiggly
    then card.shape=squiggly

'''
cards = [Card('', '', '', ''), Card('', '', '', ''), Card('', '', '', '')]
filename = "p-e-d-2.PNG"

features = {'r': 'red', 'g': 'green', 'p': 'purple', 'f': 'full', 'l': 'lines', 'e': 'empty', 'o': 'oval',
            'd': 'diamond', 's': 'squiggly', '1': 'one', '2': 'two', '3': 'three'}
i = 0
cards[1].color = features[filename[i]]
i += 2
cards[1].shading = features[filename[i]]
i += 2
cards[1].shape = features[filename[i]]
i += 2
cards[1].number = features[filename[i]]

print(cards)

