#!/usr/bin/env python3

import numpy as np
import cv2
from math import *
import colorsys
from random import randint
import sys
sys.path.append("../p3_data_lines")
from graphics import * 
# from translate import *
# from appy_transformation import *


def basicRotate(angle, axis):
    """
    Input: 
        angle of rotation in degrees
    Output:
        rotated line
    """
    theta = radians(angle)

    if axis == 'x':
        T = np.array([[1, 0, 0, 0],
                     [0, cos(theta), -sin(theta), 0], 
                     [0, sin(theta),cos(theta), 0],
                     [0,0,0, 1]])
    elif axis =='y': 
        T = np.array([[cos(theta), 0, sin(theta), 0],
                      [0, 1, 0, 0], 
                      [-sin(theta),0, cos(theta), 0],
                      [0,0,0,1]])
    elif axis == 'z':
        T = np.array([[cos(theta), -sin(theta), 0, 0], 
                      [sin(theta), cos(angle), 0, 0], 
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
    return T

if __name__ == "__main__":
    x = np.array([2, 0, 0, 1])
    H  = basicRotate(45,'z')
    print(np.dot(H.T, x.T)) 
