from graphics import * 
from input_lines import *
from rotate import *
from scale import *
from translate import *
from output_lines import *
import time

window_shape = (500,500,3)

def line():
    print("hello")
    np.random.seed(0)
    viz = Visualize(window_shape)
    
    while True: 
        option = input("1:Rotate 2:Scale 3:Translate or Q for quit ")
        x0 = int(np.random.random(size=1) * window_shape[0])
        y0 = int(np.random.random(size=1) * window_shape[1])

        x1 = int(np.random.random(size=1) * window_shape[0])
        y1 = int(np.random.random(size=1) * window_shape[1])

        datalines = [str(x0), str(y0), str(x1), str(y1)]
            
        if option == '1': 
            print("ROTATE!")
            angle = input("enter angle in deg: ")
            choice = input("rotate about a point [Y/n] ?")
            if choice == 'Y':
                point = input("enter rotation point: ")
                point = point.split()
                applyTransformation(Rotate(angle, float(point[0]), float(point[1])), datalines)
                line = Line(pt1, pt2)
                line_x, line_y = line.create("basic")
                viz.draw(line_x, line_y,color=create_unique_color_uchar(4))

            else: 
                applyTransformation( basicRotate(float(angle)), datalines)
        elif option == '2': 
            print("SCALE !")
            a = input("enter factor to scale x and y:")
            a  = a.split()
            choice = input("rotate about a point [Y/n] ? ")
            if choice =='Y':
                point = input("enter rotation point: ")
                if tr is None:
                    print("incorrect input... back to options")
                else: 
                    applyTransformation(Scale(float(a[0]),float(a[1]), float(point[0], float(point[1]))), datalines)    
            else:
                applyTransformation(basicScale(float(a[0]),float(a[1])), datalines)
        elif option == '3': 
            print("TRANSLATE!")
            p = input("Enter units to translate x and y")
            p = p.split()
            if choice is None: 
                print("incorrect input... back to options")
            else: 
                applyTransformation(basicTranslate(float(p[0]),float(p[1])), datalines)
        elif option == 'Q': 
            break
        else: 
            print("Incorrent Try again")
            continue

        cv2.imshow("Line", viz.image)
        cv2.waitKey(0)

def triangle():
    return None

def cube():
    return None

def main_menu():
    test = input("MENU \n choose something to transform with \n 1: line\n 2: triangle\n 3: cube\n" )
    # map the inputs to the function blocks
    option = { 1 : line,
               2  : triangle,
               3  : cube,
            }

    option[int(test)]()

def draw_axis(viz):
    global window_shape

    datalines = []

    x_start = (window_shape[0] - 75, 25)
    x_end =  (window_shape[0] - 50, 25) 
    y_start = (window_shape[0] - 75, 25)
    y_end = (window_shape[0] - 75, 50) 

    x_axis = str(x_start[0]) + " " + str(x_start[1])  + " " +  str(x_end[0]) + " " + str(x_end[1])
    y_axis = str(y_start[0]) + " " + str(y_start[1]) + " " + str(y_end[0]) + " " + str(y_end[1])

    datalines.append(x_axis)
    datalines.append(y_axis)

    tf_bf = applyTransformation([], datalines)
    count = 0 
    for tf_line in tf_bf:
        count +=1
        pt1, pt2 = linePairs(tf_line)[0],linePairs(tf_line)[1]
        # print(pt1,pt2)
        line = Line(pt1, pt2)
        x_l, y_l = line.create("brz")
        if count ==1: color = (255,0,0)
        elif count == 2: color = (0,0,255)
        viz.draw(x_l, y_l,color=color)

    cv2.putText(viz.image, 'x', (x_start[0] + 10, x_start[1] - 5), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), thickness=1)
    cv2.putText(viz.image, 'y', (x_start[0] - 15, x_start[1] + 10), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), thickness=1)
    

if __name__ == "__main__":
    # main_menu()
    global viz
    images = []

    # x0 = int(np.random.random(size=1) * window_shape[0])
    # y0 = int(np.random.random(size=1) * window_shape[1])

    # x1 = int(np.random.random(size=1) * window_shape[0])
    # color = int(np.random.random(size=1) * window_shape[1])
    # color2 = int(np.random.random(size=1) * window_shape[1])

    time.sleep(5)
    viz = Visualize(window_shape)
    draw_axis(viz)

    ## Before 
    print("before transformation")
    # datalines = ["200 200 300 200"]
    f = open("./input/cube.txt", "r")
    datalines = f.readlines()
    f.close()

    cx = 200 + 25
    cy = 200 + 25
    
    angle = 0
    sx = 10
    sy = 10

    tf_bf = applyTransformation([], datalines)
    count = 0 
    for tf_line in tf_bf:
        count +=1
        pt1, pt2 = linePairs(tf_line)[0],linePairs(tf_line)[1]
        # print(pt1,pt2)
        line = Line(pt1, pt2)
        x_l, y_l = line.create("brz")
        viz.draw(x_l, y_l,color=create_unique_color_uchar(1))

    # count = 0 
    # tf_scal = applyTransformation(Scale(sx, sy, cx, cy), datalines)
    # tf_trans = applyTransformation(Scale(1, 1, 500, 500), datalines)
    tf_trans = applyTransformation(basicTranslate(200,200), datalines)
    tf_scl = applyTransformation(Scale(sx, sy, cx,cy), tf_trans)

    for tf_line in tf_scl:
        count +=1
        pt1, pt2 = linePairs(tf_line)[0],linePairs(tf_line)[1]
        # print(pt1,pt2)
        line = Line(pt1, pt2)
        x_l, y_l = line.create("brz")
        viz.draw(x_l, y_l,color=create_unique_color_uchar(1))
    # for a in range(45,180,5):
    for a in range(45,360, 10):
        tf_rot = applyTransformation(Rotate(a, cx, cy), tf_scl)
        for tf_line in tf_rot:
            pt1, pt2 = linePairs(tf_line)[0],linePairs(tf_line)[1]
            # print(pt1,pt2)
            line = Line(pt1, pt2)
            x_l, y_l = line.create("brz")
            viz.draw(x_l, y_l,color=create_unique_color_uchar(a))
            # txt1 = "Computer Graphics"
            # txt2 = "Allen Spain"
            # # cv2.putText(viz.image, txt1, (5,20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), thickness=1)
            # # cv2.putText(viz.image, txt2, (5,40), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), thickness=1)
        cv2.imshow("hello",viz.image)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break        
        time.sleep(0.1)
    
    txt1 = "Computer Graphics"
    txt2 = "Allen Spain"
    cv2.putText(viz.image, txt1, (5,20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), thickness=1)
    cv2.putText(viz.image, txt2, (5,40), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), thickness=1)
    cv2.imshow("Transformed lines", viz.image)
    # cv2.imwrite("./output/ps3-cube-4.png",viz.image)
    cv2.waitKey(0)
    