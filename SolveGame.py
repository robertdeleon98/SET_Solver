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


card1 = [Card('', '', '', ''), Card('', '', '', ''), Card('', '', '', '')]
filename = ["p-e-d-2.PNG", "g-e-s-1.PNG", "r-f-s-2.PNG"]
print(len(filename))

i = 0
j = 0

for j in range(len(filename)):
    i = 0
    while filename[j][i] != '.':
        if filename[j][i] == 'r':
            card1[j].color = 'red'
        elif filename[j][i] == 'g':
            card1[j].color = 'green'
        elif filename[j][i] == 'p':
            card1[j].color = 'purple'
        elif filename[j][i] == 'f':
            card1[j].shading = 'full'
        elif filename[j][i] == 'l':
            card1[j].shading = 'lines'
        elif filename[j][i] == 'e':
            card1[j].shading = 'empty'
        elif filename[j][i] == 'o':
            card1[j].shape = 'oval'
        elif filename[j][i] == 'd':
            card1[j].shape = 'diamond'
        elif filename[j][i] == 's':
            card1[j].shape = 'squiggly'
        elif filename[j][i] == '1':
            card1[j].number = 'one'
        elif filename[j][i] == '2':
            card1[j].number = 'two'
        elif filename[j][i] == '3':
            card1[j].number = 'three'
        i += 1

for j in range(len(filename)):
    print(card1[j].color, card1[j].shading, card1[j].shape, card1[j].number)

a = 0
if card1[a].color == card1[a+1].color and card1[a].color == card1[a+2].color:
    if card1[a].shape == card1[a+1].shape and card1[a].shape == card1[a+2].shape:
        if card1[a].shading == card1[a+1].shading and card1[a].shading == card1[a+2].shading:
            if card1[a].number == card1[a+1].number and card1[a].number == card1[a+2].number:
                print("this is a set")
print("not a set")


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
# cards = Card('', '', '', '')
# filename = "p-e-d-2.PNG"
#
# features = {'r': 'red', 'g': 'green', 'p': 'purple', 'f': 'full', 'l': 'lines', 'e': 'empty', 'o': 'oval',
#             'd': 'diamond', 's': 'squiggly', '1': 'one', '2': 'two', '3': 'three'}
# i = 0
# cards.color = features[filename[i]]
# i += 2
# cards.shading = features[filename[i]]
# i += 2
# cards.shape = features[filename[i]]
# i += 2
# cards.number = features[filename[i]]
#
# print(cards)

'''
    def is_set(cards):
        for attr in cards[0].attrs.keys():
            if len(set([card.attrs[attr] for card in cards])) == 2:
                return False
        return True
'''
