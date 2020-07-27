#!/usr/bin/env python3
import numpy as np
import numpy as np
import cv2
from math import *
import colorsys
from random import randint
import sys

def basicScale(Sx, Sy, Sz):
    """
     Input: Sx and Sy floats
        are the horizontal and 
        and vertical scaling factors; center of scale 
        is at the origin of the Coordinate System
    Output:
        Matrix for scaling a vector of form [x1, y1, 1]
    """
    T = np.array([[Sx,0,0,0], 
                  [0,Sy,0,0],
                  [0,0,Sz,0], 
                  [0,0,0,1]])

    return T
    
# def Scale(Sx, Sy, Cx, Cy):
#     """
#     Input: 
#         angle of rotation in degrees
#     Output:
#         rotated line
#     """
#     t_n = basicTranslate(-Cx, -Cy)
#     T = basicScale(Sx, Sy)
#     t_p = basicTranslate(Cx, Cy)
    
#     return np.dot(np.dot(t_p, T), t_n)

if __name__ == "__main__":
    
    # x = np.array([10, 10, 1, 1])
    a = np.array([50,150,10,1])
    # print(np.dot(T, x.T))
    S = basicScale(10,10,10)
    print(np.dot(S, a.T))
    ## output [ 500 1500  100    1]
    

    


