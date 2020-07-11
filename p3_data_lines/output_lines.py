#!/usr/bin/env python3 

import numpy as np
import cv2
import math
import colorsys
from random import randint
import sys
from graphics import *
from appy_transformation import *
import os as osp

out_file = "./output/data.txt"

def Outputlines(datalines, num):
    """
    Input:
        datalines: list of ints 
    Output: 
        outputs num of data lines to a text file
    """
    global out_file

    fo = open(out_file, "w+")
    count = 0 

    if num < 0: datalines = datalines[::-1]
    # print(datalines[::-1])
    
    for line in datalines:
        if count >= abs(num):
            break 
        print('%d %d %d %d'%(line[0],line[1],line[2],line[3]),file=fo)
    
        count += 1
    print("wrote to file %s" % out_file)
    fo.close()    

if __name__ == "__main__":
    # create file for writting in 
    fi = open("./input/data.txt", "r")
    datalines = fi.readlines()
    matrix = np.eye(3, dtype=float)
    tf_data = applyTransformation(matrix, datalines)

    Outputlines(tf_data, -len(tf_data))
    

    

