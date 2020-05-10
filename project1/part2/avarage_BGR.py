import cv2
import numpy as np


def find_avarage(img):
    average = img.mean(axis=0).mean(axis=0)
    #print(average)
    return average

def findAverageChannels(img):
    b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    b = np.mean(b)
    g = np.mean(g)
    r = np.mean(r)
    return b, g, r
