#!/usr/bin/env python3 

import numpy as np
import cv2
import math
import colorsys
from random import randint
import sys
from input_lines import *
from scale_3d import *
from translate_3d import *
from rotate_3d import *
import apply_transformation_3d as ap_tf

sys.path.append("../p3_data_lines")
from graphics import *

def convert(datalines):
    data = []
    print("datalines", datalines)

    if datalines == None: 
        return None
    else:
        for line in datalines:
            line = line.split()
            # print("line after split", line)
            # print(line)
            if len(line)!=3:
                print("lines %s should be in form ['x', 'y', 'z']"%line)
                return None
            else: 
                tmp2 = np.array(line,dtype=int) # [x0, y0, x1, y1]
                data.append(tmp2) 
    print("returing", data)
    return data

def viewport(vp, ep, D, S):
    """
    vp: viewport [vsx, vsy, vcx, vcy] 
    ep: eye "cone" [xe, ye, ze]
    sp: virtual screen
    D: Distance the eye is from the viewport
    S: 1/2 the side length of the virtual screen
    Note: if the viewport size is the same as the screen, ex,ey = original point
    """
    vsx, vsy, vcx, vcy = vp 
    ex, ey, ez = ep

    
    x =  np.array([round((D * ex/(S * ez))* vsx + vcx),round((D * ey/(S * ez))* vsy + vcy),1], dtype=int)
    ### Needs to return a 4x4 matrix
    return x

if __name__ == "__main__":
    """
    The coordinates are in the eye-coordinate system with the z-axis 
    being the line of gaze (viewing direction). Assume eye distance to the center 
    of the screen is 2.5cm (D = 2.5 cm), and the physical window as well as the
    virtual screen has a side length 100cm (S = 50cm). The screen is 1000, by 1000
    And suppose the viewports pixel size is the same as the screen i.e: vsx = vsy = vcx = vcy

    """
    ### Viewport parameters
    vp = (500, 500, 500, 500)
    ep = (50, 150, 10)
    D = 2.5 # cm
    S = 50
    s = 2 # downscale window size 
    window_shape = (1000//s,1000//s,3)
    points = []

    ### example 2 house
    house =    {'I': [50, 150, 10],
                'B': [50, 0, 10],
                'C': [150, 0, 10],
                'D': [150, 0, 100],
                'E': [50, 0, 100],
                'H': [150, 150, 10],
                'G': [150, 150, 100],
                'J': [50, 150, 100],
                'A': [100, 200, 45],
                }

    ### create line segments to connect the vertices
    lines = ["IH", "HC", "CB", "BI", "JG", "GD", "DE", "EJ", "CD", "EB", "JI", "HG", "AI", "AH", "AG", "AJ"]

    viz = Visualize(window_shape)
    viz.draw_axis()
    count  = 0
    for line in lines: 
        print("------before projection------")
        print("point 1:", house[line[0]])
        H = basicRotate(360, 'z') # in degrees
        h1_t = ap_tf.applyTransPoint(H, house[line[0]])
        
        # print(h1_t)
        print("point 1 trans:", h1_t)
        # # apply perspective projction to this one point
        v1 = viewport(vp, list(h1_t[:3]), D, S)
        print("point 2:", house[line[1]])
        h2_t = ap_tf.applyTransPoint(H, house[line[1]])
        print("point 1 trans:", h2_t)
        v2 = viewport(vp, list(h2_t[:3]), D, S)
        print("------after projection------")
        pt1 = (v1[0]//s, v1[1]//s)
        pt2 = (v2[0]//s, v2[1]//s)
        print("pt1 %s, pt2 %s"%(pt1,pt2))

        line = Line(pt1, pt2)
        line.id = count
        line.line_color = create_unique_color_uchar(count)
        x_l, y_l = line.create("brz")
        print("color", create_unique_color_uchar(count))
        viz.draw(x_l, y_l, color=create_unique_color_uchar(count))
        count +=1

    cv2.imshow("Scale", viz.image)
    cv2.imwrite("./output/ps4-4-c-4.png",viz.image)
    cv2.waitKey(0)

    ## example 1 - cube
    cube = {    'I': [50, 150, 10],
                'B': [50, 0, 10],
                'C': [150, 0, 10],
                'D': [150, 0, 100],
                'E': [50, 0, 100],
                'H': [150, 150, 10],
                'G': [150, 150, 100],
                'J': [50, 150, 100]
               }
    ### create line segments to connect the vertices
    lines = ["IH", "HC", "CB", "BI", "JG", "GD", "DE", "EJ", "DC", "EB", "IJ", "GH"]
    # print("LENGTH", len(lines))
    # viz = Visualize(window_shape)
    # viz.draw_axis()
    # count  = 0
    # for line in lines: 
    #     print("------before projection------")
    #     print("point 1:", cube[line[0]])
    #     v1 = viewport(vp, cube[line[0]], D, S)
    #     print("point 2:", cube[line[1]])
    #     v2 = viewport(vp, cube[line[1]], D, S)
    #     print("------after projection------")
    #     pt1 = (v1[0]//s, v1[1]//s)
    #     pt2 = (v2[0]//s, v2[1]//s)
    #     print("pt1 %s, pt2 %s"%(pt1,pt2))

    #     line = Line(pt1, pt2)
    #     line.id = count
    #     line.line_color = create_unique_color_uchar(count)
    #     x_l, y_l = line.create("brz")
    #     viz.draw(x_l, y_l, color=create_unique_color_uchar(count))
        
    #     count +=1

    # # # cv2.imwrite("./output/ps4-2-a-0.png",viz.image)
    # cv2.imshow("projective projection", viz.image)
    # cv2.waitKey(0)

    
        


    #     line = Line(v1[:2],v2[:2])
    #     line.id = 1 
    #     line.line_color = create_unique_color_uchar(line.id)
    #     x_l, y_l = line.create("brz")
    #     viz.draw(x_l, y_l)

    # cv2.imshow("projective projection", viz.image)
    # cv2.waitKey(0)

    # f.close()
    
        
        # find point project it move to the next lin
        

    # id = 0
    # viz = Visualize(window_shape)
    # for vertex in shape: 
    #     ep = (vertex[0], vertex[1], vertex[2])
    #     print("3d edge", ep)
    #     print("2d projection", viewport(vp, ep, D, S))
    #     v = viewport(vp, ep, D, S)
    #     # print(v)
    #     points.append((v[0]//2, v[1]//2))
    
    # # for i in range(len(points) - 1):
    # #     if i == 0: 
    #         pt1 = points[i] # 
    #         pt2 = points[i + 1] # 1
    #     else: 
    #         pt1 = pt2 # 1
    #         pt2 = points[i + 1] # 2
    #     print("pt1 %s, pt2 %s"%(pt1,pt2))
    #     line = Line(pt1,pt2)
    #     line.id = i 
    #     line.line_color = create_unique_color_uchar(line.id)
    #     x_l, y_l = line.create("brz")
    #     # print(x_l)
        # print(y_l)
    #     viz.draw(x_l, y_l)
    
    # cv2.imshow("projective projection", viz.image)
    # cv2.waitKey(0)

    # f.close()