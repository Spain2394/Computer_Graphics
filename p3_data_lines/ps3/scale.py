#!/usr/bin/env python3

from translate import *


def basicScale(Sx, Sy):
    """
     Input: Sx and Sy floats
        are the horizontal and 
        and vertical scaling factors; center of scale 
        is at the origin of the Coordinate System
    Output:
        Matrix for scaling a vector of form [x1, y1, 1]
    """
    T = np.array([[Sx,0,0], [0,Sy,0], [0,0,1]])

    return T
    
def Scale(Sx, Sy, Cx, Cy):
    """
    Input: 
        angle of rotation in degrees
    Output:
        rotated line
    """
    t_n = basicTranslate(-Cx, -Cy)
    T = basicScale(Sx, Sy)
    t_p = basicTranslate(Cx, Cy)
    
    return np.dot(np.dot(t_p, T), t_n)

if __name__ == "__main__":
    
    x = np.array([10, 10, 1])
    # print(np.dot(T, x.T))
    H = Scale(2,2,0,0)
    print(np.dot(H, x.T))
    

    


