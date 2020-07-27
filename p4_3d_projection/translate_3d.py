#!/usr/bin/env python3

import numpy as np
import cv2
import math
import colorsys
from random import randint
import sys


def basicTranslate(Tx, Ty, Tz):
    """
    Input: 
        Tx, Ty translation in the x and y directions
    Output:
        Transformed output point
    """
    T = np.array([[1,0,0,Tx],
                 [0,1,0, Ty],
                 [0,0,1, Tz],  
                 [0,0,0, 1]])

    return T


if __name__ == "__main__":
    x = np.array([10, 10, 1, 1])
    # print(np.dot(T, x.T))
    H = basicTranslate(2,2,2)
    print(np.dot(H, x.T))