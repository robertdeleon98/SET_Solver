# import numpy as np
# import pandas as pd
# import cv2
# import os
import time
import itertools
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

start_time = time.time_ns()

card = []
for i in range(12):
    card.append(Card('', '', '', ''))
filename = ["r-e-d-3.PNG",
            "g-f-o-3.PNG",
            "p-l-s-3.PNG",
            "g-e-d-1.PNG",
            "g-e-s-1.PNG",
            "p-e-d-2.PNG",
            "p-e-o-2.PNG",
            "p-f-o-3.PNG",
            "p-l-d-1.PNG",
            "r-f-s-2.PNG",
            "r-l-d-2.PNG",
            "r-l-s-1.PNG"]
print(len(filename))

i = 0
j = 0

for j in range(len(filename)):
    i = 0
    while filename[j][i] != '.':
        if filename[j][i] == 'r':
            card[j].color = 'red'
        elif filename[j][i] == 'g':
            card[j].color = 'green'
        elif filename[j][i] == 'p':
            card[j].color = 'purple'
        elif filename[j][i] == 'f':
            card[j].shading = 'full'
        elif filename[j][i] == 'l':
            card[j].shading = 'lines'
        elif filename[j][i] == 'e':
            card[j].shading = 'empty'
        elif filename[j][i] == 'o':
            card[j].shape = 'oval'
        elif filename[j][i] == 'd':
            card[j].shape = 'diamond'
        elif filename[j][i] == 's':
            card[j].shape = 'squiggly'
        elif filename[j][i] == '1':
            card[j].number = 'one'
        elif filename[j][i] == '2':
            card[j].number = 'two'
        elif filename[j][i] == '3':
            card[j].number = 'three'
        i += 1

# for j in range(len(filename)):
#     print(card[j].color, card[j].shading, card[j].shape, card[j].number)

for subset in itertools.combinations(card, 3):
    for j in range(len(subset)):
        print(subset[j].color, subset[j].shading, subset[j].shape, subset[j].number)

    a = 0
    if (subset[a].color == subset[a+1].color and subset[a].color == subset[a+2].color) or (subset[a].color != subset[a+1].color and subset[a].color != subset[a+2].color):
        if (subset[a].shape == subset[a+1].shape and subset[a].shape == subset[a+2].shape) or (subset[a].shape != subset[a+1].shape and subset[a].shape != subset[a+2].shape):
            if (subset[a].shading == subset[a+1].shading and subset[a].shading == subset[a+2].shading) or (subset[a].shading != subset[a+1].shading and subset[a].shading != subset[a+2].shading):
                if (subset[a].number == subset[a+1].number and subset[a].number == subset[a+2].number) or (subset[a].number != subset[a+1].number and subset[a].number != subset[a+2].number):
                    print("this is a set\n")
                    card_set = subset
                    break
                else:
                    print("this is not a set\n")
            else:
                print("this is not a set\n")
        else:
            print("this is not a set\n")
    else:
        print("this is not a set\n")
'''
SET Rules
They all have the same color or have three different colors.
They all have the same shading or have three different shadings.
They all have the same shape or have three different shapes.
They all have the same number or have three different numbers.
'''



end_time = time.time_ns()

total_time = end_time - start_time
print(total_time / (10**9))
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
