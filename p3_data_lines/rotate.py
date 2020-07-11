#!/usr/bin/env python3

import numpy as np
import cv2
from math import *
import colorsys
from random import randint
import sys
from graphics import *
from translate import *
from appy_transformation import *


def basicRotate(angle):
    """
    Input: 
        angle of rotation in degrees
    Output:
        rotated line
    """
    # pt1 = (1,1)

    # x = np.array([pt1[0], pt1[1], 1])
    T = np.array([[cos(radians(angle)),-sin(radians(angle)), 0], [sin(radians(angle)),cos(radians(angle)), 0], [0,0,1]])

    return T

def Rotate(angle, Cx, Cy):
    """
    Input: 
        angle of rotation in degrees
    Output:
        rotated line
    """

    t_n = basicTranslate(-Cx, -Cy)
    T = basicRotate(angle)
    t_p = basicTranslate(Cx, Cy)
    

    return np.dot(np.dot(t_p, T), t_n)


if __name__ == "__main__":
    # Edges are defined as having two defined points
    # Transformations are done on each individual point vector
    # pt1 = (1,1

    # check 1
    x = np.array([1, 1, 1])
    H  = Rotate(45, 2,2 )
    print(np.dot(H.T, x.T)) 
    ## output: [0.58578644 2.         1.        ]

    # check 2
    x = np.array([3, 1, 1])
    H  = Rotate(45, 2,2 )
    print(np.dot(H.T, x.T)) 
    ## output: [0.58578644 2.         1.        ]

    ## check 3
    x = np.array([2, 3, 1])
    H  = Rotate(45, 2,2 )
    print(np.dot(H.T, x.T)) 
    ## output: [2.70710678 2.70710678 1.        ]

    
    
    


