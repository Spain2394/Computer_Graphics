#!/bin/usr/env python3 

import numpy as np
import cv2
import math
import colorsys
from random import randint
import sys
from graphics import *

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

    if datalines == None: 
        return None
    else:
        for line in datalines:
            line = line.split()
            if len(line)!=4:
                print("lines %s should be in form ['x1','x2','x3','x5']"%line)
                return None
            else: 
                tmp2 = np.array(line,dtype=int) # [x0, y0, x1, y1]
                data.append(tmp2) 
    return data

def applyTransPoint(matrix, point):
    tf_pt = []
    if matrix.shape != (3,3):
        print("Matrix dimensions are not correct")
        return None
    else:
        tmp = np.array([point[0], point[1], 1])
        tf_pt = np.dot(tmp, matrix)
    return tf_pt
def applyTransformation(matrix, datalines):
    """
    Applies single transformation matrix to each line in datalines
    --
    Input: 
    matrix of floats is a 4x4 matrix representing the transformations 
    that should be applied to each line in datalines
    datalines is a list of ints that represent lines in form x0,y0,x1,1
    Output: 
    transformed list of datalines? 
    """ 
    trans_data = []
    data_converted = convert(datalines)
    
    if matrix.shape != (3,3):
        print("incorrect matrix dimensions")
        return None

    for line in data_converted:
        try: 
            tf_pt1 = applyTransPoint(matrix, line[:2]) 
            tf_pt2 = applyTransPoint(matrix, line[2:])
            trans_data.append(np.append(tf_pt1[:2],tf_pt2[:2]))
        except ValueError or TypeError:
            print("cannot convert point to list to int")
            return None

    return trans_data

def rndConv(num):
    return int(round(num))
    
def linePairs(line):
    pt1 = (rndConv(line[0]),rndConv(line[1]))
    pt2 = (rndConv(line[2]),rndConv(line[3]))

    return pt1, pt2

if __name__ == "__main__":

    window_shape = (500,500,3) # create blank slate

    f = open("./input/data.txt", "r")
    datalines = f.readlines()
    matrix = np.eye(3, dtype=float)
    # matrix = np.array([[0.7, -0.7, 0],[0.7, 0.7, 0],[-0.8, 2, 1]])
    assert matrix.shape == (3,3)
    tf_data = applyTransformation(matrix, datalines)
    print(tf_data)
    
    # instatiate blank image to draw on
    viz = Visualize(window_shape)

    traingle = Shape()

    for tf_line in tf_data:
        
        pt1, pt2 = linePairs(tf_line)[0],linePairs(tf_line)[1]
        print(pt1,pt2)
        line = Line(pt1, pt2)
        traingle.add(line)

    # draw a triangle
    for edge in traingle.edges:
        x_l, y_l = edge.create("brz")
        print(x_l, y_l)
        # print(x_l, y_l)
        viz.draw(x_l,y_l)  

    # complete picture after all lines have been added    
    cv2.imwrite("./output/ps3-trans-a.png",viz.image)
    cv2.imshow("Basic Alg", viz.image)
    cv2.waitKey(0)
    f.close() # close file
    
    # for i in range(len(traingle.edge_ids)):
    #     edge_color = create_unique_color_uchar(i)
    #     line_x, line_y = traingle.edges[i].create("brz")
    #     viz.draw(line_x, line_y, color=edge_color)
        
    # cv2.imwrite("./output/ps3-a-trans.png",viz.image)
    # cv2.imshow("2a", viz.image)
    # cv2.waitKey(0)
    
    
        
    
    # line = Line(pt1, pt2)
    # shape = Shape(line)
    # line_x, line_y = line.create("basic")
    # # line_x, line_y = line.basic_alg(pt1[0], pt1[1], pt2[0], pt2[1])
    

    # print(pt1)
    # print(pt2)
    # line = Lines(pt1,pt2)
    # line.id = 1
    # line.line_color = create_unique_color_uchar(line.id)
    # line.create(func="brz")
    # line_x, line_y = line.basic_alg(pt1[0], pt1[1], pt2[0], pt2[1])
    # viz.draw_line(line_x, line_y)

    # pt1 = (rndConv(tf_data[1][0]), rndConv(tf_data[1][1]))
    # pt2 = (rndConv(tf_data[1][2]), rndConv(tf_data[1][3]))
    # print(pt1)
    # print(pt2)
    # line = Lines(pt1,pt2)
    # line.id = 2
    # line.line_color = create_unique_color_uchar(line.id)
    # line_x, line_y = line.basic_alg(pt1[0], pt1[1], pt2[0], pt2[1])
    # viz.draw_line(line_x, line_y)

    # pt1 = (rndConv(tf_data[2][0]), rndConv(tf_data[2][1]))
    # pt2 = (rndConv(tf_data[2][2]), rndConv(tf_data[2][3]))
    # print(pt1)
    # print(pt2)
    # line = Lines(pt1,pt2)
    # line.id = 3
    # line.line_color = create_unique_color_uchar(line.id)
    # line_x, line_y = line.basic_alg(pt1[0], pt1[1], pt2[0], pt2[1])
    # viz.draw_line(line_x, line_y)

    ## lines has Points 
    ## When you display you display all lines

