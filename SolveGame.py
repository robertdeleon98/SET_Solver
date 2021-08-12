'''
SET Rules
They all have the same number or have three different numbers.
They all have the same shape or have three different shapes.
They all have the same shading or have three different shadings.
They all have the same color or have three different colors.
'''

import numpy as np
import pandas as pd
import cv2
import os
from random import shuffle
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread, imshow, subplots, show

number = ['one', 'two', 'three']
shape = ['oval', 'diamond', 'squiggly']
shading = ['full', 'striped', 'empty']
color = ['red', 'green', 'purple']




image = imread('image-data/positive-images/r-f-s-2.PNG')
images = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
imshow(images[0])
show()

'''
read image name and extract features from image file name
if color = red
    then card.color=red
if shape = squiggly
    then card.shape=squiggly

'''
