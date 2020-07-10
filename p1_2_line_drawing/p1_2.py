#!/bin/usr/env python3 

import numpy as np
import cv2
import math
import colorsys
from random import randint
import time

## Allen Spain June 07, 2020 
## P1-2
## CSCI 6810

## class structure ispired by https://github.com/nwojke/deep_sort/blob/master/application_util/image_viewer.py

"""
Coordinate system that will be used in this program
0/0---column--->
 |
 |
row
 |
 |
 v
"""

# general utility functions for generating different colors
def create_unique_color_float(tag, hue_step = 0.41):
    h, v = (tag * hue_step) % 1, 1. - (int(tag * hue_step) % 4) / 5.
    r, g, b = colorsys.hsv_to_rgb(h, 1., v)
    return r, g, b

def create_unique_color_uchar(tag, hue_step=0.41):

    r, g, b = create_unique_color_float(tag, hue_step)
    
    color = int(255*r), int(255*g), int(255*b)
    return color

class Visualize(object):
    def __init__(self, shape, color = (255,255,255)):
        self.window_shape = shape
        self.color = color
        self.image = np.zeros(self.window_shape, dtype=np.uint8)
        # image=np.zeros((h,w,3),np.uint8)

    def draw_line(self, line_x, line_y, thickness = 1, color = (255,0,0)):
        """
        input:
            line_x: uint
            line_y: uint
            points that represent a line
        output: 
            image: this draws on this image
        """

        # rows cols
        for cols,rows in zip(line_x,line_y):
            if cols < self.window_shape[0] and rows < self.window_shape[1]:
                self.image[cols][rows] = color        

class Lines(object):

    def __init__(self, pt1, pt2, thickness = 1, length = 0, line_color = (255,0,0)):
        self.vertices = (pt1, pt2)
        self.pt1 = pt1
        self.pt2 = pt2
        self.len = length
        self.thickness = thickness
        self.line_color = line_color
        self.id = 0

    def basic_alg(self,x0, y0, x1, y1):

        """ 
        intput: x0, y0, x1, y1 are ints and represent the endpoints of a line
        use basic algebra (y = mx + b) for creating a line that passes through the endpoints
        output: line_x, line_y lists containing all the ints that makeup the line
        """ 


        line_x = []
        line_y = []

        dx = x1 - x0
        dy = y1 - y0

        if abs(dy) < abs(dx): 
            stp = abs(dx)
        else: 
            stp = abs(dy)
    
        y = y0 
        x = x0

        xi = dx/stp
        yi = dy/stp

        # #  increase or dec from x0/y0 --> x1/y1
        # if y1 < y0:  
        #     yi = -yi
        #     dy = -dy
        # if x1 < x0: 
        #     xi = -xi
        #     dx = -dx
            
        # start at last point go to first point

        print("xincrement", xi)
        print("yincrement", yi)

        for i in range(stp):
            x = x + xi
            y = y + yi
            line_x.append(int(x))
            line_y.append(int(y))

        return line_x, line_y


    def brzlow(self, x0, y0, x1, y1):
        line_x = []
        line_y = []
        
        dx = x1 - x0 
        dy = y1 - y0 

        yi = 1 
        if dy <  0: 
            yi = -1 
            dy = - dy
        
        err = 2 * dy - dx
        y = y0

        print("not entering")
        for x in range(x0, x1):
            print("entering")
            line_x.append(int(x))
            line_y.append(int(y))
            
            if err > 0: 
                y = y + yi
                err = err - 2 * dx
            err = err + 2 * dy
    
        return line_x, line_y

    def brzhigh(self, x0, y0, x1, y1):

        print("Hello")
        line_x = []
        line_y = []

        dx = x1 - x0 
        dy = y1 - y0 

        xi = 1 
        if dx < 0: 
            xi = -1 
            dx = - dx
        x = x0
        
        err = 2 * dx - dy

        print("not entering loop")
    
        for y in range(y0, y1):
            print("entering loop")
            
            line_x.append(int(x))
            line_y.append(int(y))
            if err > 0: 
                x = x + xi
                err = err - 2 * dy
            print("err", err)
            err = err + 2 * dx

        # print(line_x, line_y)
        return line_x, line_y

    #  https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
    def brz(self, x0, y0, x1, y1):

        """ 
        intput: x0, y0, x1, y1 are ints and represent the endpoints of a line
        this function implements the "Bresenham" algorithm for creating a line that passes through the endpoints
        output: line_x, line_y lists containing all the ints that makeup the line
        """ 

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        
        if dy < dx: 
            print("low")
            if x0 > x1:
                line_x, line_y = self.brzlow(x1,y1,x0,y0)  # plot line low (x1, y1, x0, y0) # flip the order

            else: 
                line_x, line_y = self.brzlow(x0,y0,x1,y1) # plot line low (x0, y0, x1, y1) # flip the order
        else:  # dy not greater than dx 
            print("negative slope")
            if y0 > y1: 
                line_x, line_y = self.brzhigh(x1,y1,x0,y0) # plot line high (x1,y1, x0, y0)
            else: 
                line_x, line_y = self.brzhigh(x0,y0,x1,y1) # plot line high (x0,y0, x1,y1)

        return line_x, line_y
                
if __name__ == "__main__":
    # parameters are points and window dimensions
    # units are in pixels
    # pt1 = (100, 100)
    # pt2 = (200, 200)
    window_shape = (400,300,3)
    np.random.seed(0)

    # ###########################
    # # P1-1 Basic algebra
    # ###########################
    # # N: number of lines to draw
    N = int(input("How many lines do you want to draw: "))

    if N is None:
        print("incorrect input")
        exit()
        
    viz = Visualize(window_shape)    
    # viz.draw_line(line_x, line_y,color=line.line_color)
    start = time.time()
    for i in range(N):
        
        x0 = int(np.random.random(size=1) * window_shape[0])
        y0 = int(np.random.random(size=1) * window_shape[1])
        print("x0,y0", (x0,y0))

        x1 = int(np.random.random(size=1) * window_shape[0])
        y1 = int(np.random.random(size=1) * window_shape[1])
        print("x1,y1", (x1,y1))
        pt1 =  (x0, y0)
        pt2 =  (x1, y1)

        line = Lines(pt1, pt2)
        line.id = i 
        line.line_color = create_unique_color_uchar(line.id)

        line_x, line_y = line.basic_alg(pt1[0], pt1[1], pt2[0], pt2[1])
        viz.draw_line(line_x, line_y,color=line.line_color)
    print("it took %.5f milli seconds to process %.f lines" % ((time.time() - start)/1000.0, N))

    cv2.imwrite("./output/ps1-1-many.png",viz.image)
    cv2.imshow("Basic alg", viz.image)
    cv2.waitKey(0)


    # 1a (10,10,10,30)
    # a = [(10, 10, 30, 10),
    # (10, 10, 10, 30), 
    # (30, 10, 10, 10), 
    # (10, 30, 10, 10), 
    # (10, 10, 20, 30), 
    # (10, 30, 20, 10), 
    # (20, 30, 10, 10), 
    # (20, 10, 10, 30)]
    # point = {1:"a", 2: "b", 3:"c", 4:"d", 5:"e", 6:"f", 7: "g", 8:"h"}
    viz = Visualize(window_shape)
    

    line1 = Lines((0,0), (1,1))
    line1.id = 1
    line1.line_color = create_unique_color_uchar(line1.id)
    line_x, line_y = line1.brz(10, 10, 30, 10)
    viz.draw_line(line_x, line_y,color=line1.line_color)
    line_x, line_y = line1.brz(10, 10, 10, 30)
    viz.draw_line(line_x, line_y,color=line1.line_color)
    line_x, line_y = line1.brz(10, 30, 10, 10) 
    viz.draw_line(line_x, line_y,color=create_unique_color_uchar(1))

    line_x, line_y = line1.brz(10, 30, 30, 30)
    viz.draw_line(line_x, line_y,color=create_unique_color_uchar(2))

    line_x, line_y = line1.brz(30, 30, 30, 10)
    viz.draw_line(line_x, line_y,color=create_unique_color_uchar(3))

    line_x, line_y = line1.brz(10, 10, 30, 10)
    viz.draw_line(line_x, line_y,color=create_unique_color_uchar(4))

    # # diagonals 
    line_x, line_y = line1.brz(30, 30, 40, 40)
    # dx = 10 
    # dy = 10 
    viz.draw_line(line_x, line_y,color=create_unique_color_uchar(5))

    # # diagonals 
    line_x, line_y = line1.brz(10, 10, 20, 20)
    viz.draw_line(line_x, line_y,color=create_unique_color_uchar(6))

    # # diagonals 
    line_x, line_y = line1.brz(30, 10, 40, 20)
    viz.draw_line(line_x, line_y,color=create_unique_color_uchar(7))

    # # diagonals 
    line_x, line_y = line1.brz(10, 30, 20, 40)
    viz.draw_line(line_x, line_y,color=create_unique_color_uchar(8))

    # # back squares
    line_x, line_y = line1.brz(20, 20, 40, 20)
    viz.draw_line(line_x, line_y,color=create_unique_color_uchar(8))

    # # back squares
    line_x, line_y = line1.brz(40, 20, 40, 40)
    viz.draw_line(line_x, line_y,color=create_unique_color_uchar(9))

    # # back squares
    line_x, line_y = line1.brz(40, 40, 20, 40)
    viz.draw_line(line_x, line_y,color=create_unique_color_uchar(10))

    # back squares
    line_x, line_y = line1.brz(20, 40, 20, 20)
    viz.draw_line(line_x, line_y,color=create_unique_color_uchar(11))

    cv2.imwrite("./output/ps1-2-square.png",viz.image)
    cv2.imshow("2a", viz.image)
    cv2.waitKey(0)

    # overall sctucture:  
    # line inherets array of Points
    # Polygon inherits an array of Lines
    #   apply polygon operations translate, rotate, scale
    # visualize lines 
    


    ##########################
    # P1-2 Bresenham algorithm
    ###########################
    
    # N = int(input("How many lines do you want to draw: "))

    # if N is None:
    #     print("incorrect input")
    #     exit()
        
    # viz = Visualize(window_shape)    
    # # viz.draw_line(line_x, line_y,color=line.line_color)
    # for i in range(N):
        
    #     x0 = int(np.random.random(size=1) * window_shape[0])
    #     y0 = int(np.random.random(size=1) * window_shape[1])
    #     print("x0,y0", (x0,y0))

    #     x1 = int(np.random.random(size=1) * window_shape[0])
    #     y1 = int(np.random.random(size=1) * window_shape[1])
    #     print("x1,y1", (x1,y1))
    #     pt1 =  (x0, y0)
    #     pt2 =  (x1, y1)

    #     line = Lines(pt1, pt2)
    #     line.id = i 
    #     line.line_color = create_unique_color_uchar(line.id)

    #     line_x, line_y = line.brz(pt1[0], pt1[1], pt2[0], pt2[1])
    #     viz.draw_line(line_x, line_y,color=line.line_color)
    #     cv2.imshow("Hello", viz.image)

    # # write 
    # cv2.imwrite("./output/ps1-2.png",viz.image)
    # # cv2.imshow("B", viz.image)
    
    # # # press any key to exit
    # cv2.waitKey(0)

    # # N: number of lines to draw
    # N = int(input("How many lines do you want to draw: "))

    # if N is None:
    #     print("incorrect input")
    #     exit()
        
    # viz = Visualize(window_shape)    
    # # viz.draw_line(line_x, line_y,color=line.line_color)
    # for i in range(N):
        
    #     x0 = int(np.random.random(size=1) * window_shape[0])
    #     y0 = int(np.random.random(size=1) * window_shape[1])
    #     print("x0,y0", (x0,y0))

    #     x1 = int(np.random.random(size=1) * window_shape[0])
    #     y1 = int(np.random.random(size=1) * window_shape[1])
    #     print("x1,y1", (x1,y1))
    #     pt1 =  (x0, y0)
    #     pt2 =  (x1, y1)

    #     line = Lines(pt1, pt2)
    #     line.id = i 
    #     line.line_color = create_unique_color_uchar(line.id)

    #     line_x, line_y = line.basic_alg(pt1[0], pt1[1], pt2[0], pt2[1])
    #     viz.draw_line(line_x, line_y,color=line.line_color)

    # # write 
    # cv2.imwrite("./output/ps1-a.png",viz.image)
    # cv2.imshow("Bresenham", viz.image)
    
    # # # press any key to exit
    # cv2.waitKey(0)

    
