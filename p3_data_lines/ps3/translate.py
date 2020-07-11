#!/usr/bin/env python3

import numpy as np
import cv2
import math
import colorsys
from random import randint
import sys
from graphics import *


def basicTranslate(Tx, Ty):
    """
    Input: 
        Tx, Ty translation in the x and y directions
    Output:
        Transformed output point
    """
    T = np.array([[1,0,Tx], [0,1,Ty], [0,0,1]])

    return T


if __name__ == "__main__":
    print(basicTranslate(20,40))
    

    


