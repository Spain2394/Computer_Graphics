#!/usr/bin/env python3 

import numpy as np
import cv2
import math
import colorsys
from random import randint
import sys
from scale_3d import *

# sys.path.append("/Users/allenspain/Documents/Courses/2020/CSCI 6810/")
# from p1_2_line_drawing.p1_2 import *

# from input_lines import *

## Allen Spain June 13, 2020 
## P3 
## CSCI 6810


# convert datalines into a list of ints
# all arrays are going to be transformed into numpy int arrays

def convert(datalines):
    data = []
    print("datalines", datalines)

    if datalines == None: 
        return None
    else:
        for line in datalines:
            line = line.split()
            print("line after split", line)
            if len(line)!=4:
                print("lines %s should be in form ['x1','x2','x3','x5']"%line)
                return None
            else: 
                tmp2 = np.array(line,dtype=int) # [x0, y0, x1, y1]
                data.append(tmp2) 
    print("returing", data)
    return data


# TODO check in puts
def applyTransPoint(matrix, point):
    tf_pt = []
    if matrix.shape != (4, 4):
        print("matrix shape", matrix.shape )
        print("Matrix dimensions are not correct")
        return None
    else:
        x = np.array([point[0], point[1], point[2], 1])
    return np.dot(matrix, x.T)
# def applyTransformation(matrix, datalines):
#     """
#     Applies single transformation matrix to each line in datalines
#     --
#     Input: 
#     matrix of floats is a 4x4 matrix representing the transformations 
#     that should be applied to each line in datalines
#     datalines is a list of ints that represent lines in form x0,y0,x1,1
#     Output: 
#     transformed list of datalines? 
#     """ 
#     trans_data = []

#     if datalines is None: 
#         return None
#     elif type(datalines[0]).__module__ == np.__name__:
#         data_converted = datalines
#     else:
#         data_converted = convert(datalines)
    
#     if len(matrix) == 0:
#         matrix = np.eye(3, dtype=float)
#     elif matrix.shape != (4,4):
#         print("incorrect matrix dimensions")
#         return None


#     for line in data_converted:
#         try: 
            
#             tf_pt1 = applyTransPoint(matrix, line[:3]) 
#             tf_pt2 = applyTransPoint(matrix, line[3:])
#             trans_data.append(np.append(tf_pt1[:3],tf_pt2[:3]))

#             # # trans_data = np.vstack()

#         except ValueError or TypeError:
#             print("cannot convert point to list to int")
#             return None

#     return trans_data

# def rndConv(num):
#     return int(round(num))
    
# def linePairs(line):
#     pt1 = (rndConv(line[0]),rndConv(line[1]))
#     pt2 = (rndConv(line[2]),rndConv(line[3]))

#     return pt1, pt2



if __name__ == '__main__':
    a = [50, 150, 10]
    S = basicScale(10, 10, 10)
    print(applyTransPoint(S,a))
    print(type(applyTransPoint(S,a)))
    
    
    # print(np.dot(H, x.T))

    