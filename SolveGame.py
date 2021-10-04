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
filename = ["g-f-o-1x123-412_345-637.PNG",
            "r-f-o-3x.PNG",
            "r-f-d-2x.PNG",
            "p-f-s-1x.PNG",
            "r-l-o-3x.PNG",
            "g-l-o-2x.PNG",
            "g-e-d-1x.PNG",
            "p-f-o-3x.PNG",
            "r-e-s-3x.PNG",
            "g-e-s-3x.PNG",
            "r-f-d-1x.PNG",
            "p-e-o-3x.PNG"]
print(len(filename))

i = 0
j = 0

for j in range(len(filename)):
    i = 0
    '''
    while filename[j][i] != 'x':
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
    '''
    while filename[j][i] != 'x':
        card[j].color = filename[j][i]
        print(card[j].color)
        i += 2
        card[j].shading = filename[j][i]
        print(card[j].shading)
        i += 2
        card[j].shape = filename[j][i]
        print(card[j].shape)
        i += 2
        card[j].number = filename[j][i]
        print(card[j].number)
        i += 1
# for j in range(len(filename)):
#     print(card[j].color, card[j].shading, card[j].shape, card[j].number)

'''
SET Rules
They all have the same color or have three different colors.
They all have the same shading or have three different shadings.
They all have the same shape or have three different shapes.
They all have the same number or have three different numbers.
'''
for subset in itertools.combinations(card, 3):
    for j in range(len(subset)):
        print(subset[j].color, subset[j].shading, subset[j].shape, subset[j].number)

    a = 0
    if (subset[a].color == subset[a+1].color and subset[a].color == subset[a+2].color and subset[a+1].color == subset[a+2].color) or (subset[a].color != subset[a+1].color and subset[a].color != subset[a+2].color and subset[a+1].color != subset[a+2].color):
        if (subset[a].shape == subset[a+1].shape and subset[a].shape == subset[a+2].shape and subset[a+1].shape == subset[a+2].shape) or (subset[a].shape != subset[a+1].shape and subset[a].shape != subset[a+2].shape and subset[a+1].shape != subset[a+2].shape):
            if (subset[a].shading == subset[a+1].shading and subset[a].shading == subset[a+2].shading and subset[a+1].shading == subset[a+2].shading) or (subset[a].shading != subset[a+1].shading and subset[a].shading != subset[a+2].shading and subset[a+1].shading != subset[a+2].shading):
                if (subset[a].number == subset[a+1].number and subset[a].number == subset[a+2].number and subset[a+1].number == subset[a+2].number) or (subset[a].number != subset[a+1].number and subset[a].number != subset[a+2].number and subset[a+1].number != subset[a+2].number):
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

set_list = []
for i in range(len(card_set)):
    print(card_set[i].color, card_set[i].shading, card_set[i].shape, card_set[i].number)
    set_list.append(str(card_set[i].color)+'-'+str(card_set[i].shading)+'-'+str(card_set[i].shape)+'-'+str(card_set[i].number))
print(set_list)


end_time = time.time_ns()

total_time = end_time - start_time
print(total_time / (10**9))

