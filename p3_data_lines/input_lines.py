#!/bin/usr/env python3 

import numpy as np
import cv2
import math
import colorsys
from random import randint
import time

## Allen Spain June 13, 2020 
## P3 
## CSCI 6810

"""
Coordinate system that will be used in this program
Note: this graph will be flipped about the x axis when comparing
with conventional graphs y facing upwards. To check you answers
simply invert your y --> -y values. This will allow you to check your answers
0/0---column--->
 |
 |
row
 |
 |
 v
"""


def inputLines(datalines, num):
    """
    Input: datalines filename representing lines. ie the first line is of the form: 
    x0 y0 x1 y1. four integers 
    Reads datalines from an external file (name of file is provided by the user). On
    return num will contain the number of lines read from the file.
    output: num which is an int of the number of lines.
    """ 
    num_lines = 0

    if datalines is not None:
        if num >= 0:
            if datalines[num - 1] is not None: 
                num_lines = num
        else: num_lines = abs(num)
    else: return None
    
    return num_lines
        
    
if __name__ == "__main__":

    f = open("./input/data.txt", "r")

    datalines = f.readlines()

    # NEGATIVE IS HANDLED AS NUM OF POINTS FROM THE END OF THE FILE
    print(inputLines(datalines, -1))
    
    f.close() # close file