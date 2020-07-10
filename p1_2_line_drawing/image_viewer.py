#!/usr/bin/env python3
import numpy as np
import cv2
import time

class ImageViewer(object):
    """An image viewer with drawing routines and video capture capabilities.
    Key Bindings:
    * 'SPACE' : pause
    * 'ESC' : quit
    Parameters
    ----------
    update_ms : int
        Number of milliseconds between frames (1000 / frames per second).
    window_shape : (int, int)
        Shape of the window (width, height).
    caption : Optional[str]
        Title of the window.
    Attributes
    ----------
    image : ndarray
        Color image of shape (height, width, 3). You may directly manipulate
        this image to change the view. Otherwise, you may call any of the
        drawing routines of this class. Internally, the image is treated as
        beeing in BGR color space.
        Note that the image is resized to the the image viewers window_shape
        just prior to visualization. Therefore, you may pass differently sized
        images and call drawing routines with the appropriate, original point
        coordinates.
    color : (int, int, int)
        Current BGR color code that applies to all drawing routines.
        Values are in range [0-255].
    text_color : (int, int, int)
        Current BGR text color code that applies to all text rendering
        routines. Values are in range [0-255].
    thickness : int
        Stroke width in pixels that applies to all drawing routines.

    """

    def __init__(self, update_ms, window_shape=(640, 480), caption="Figure 1"):
        self._window_shape = window_shape
        self._caption = caption
        self._update_ms = update_ms
        self._video_writer = None
        self._user_fun = lambda: None
        self._terminate = False

        self.image = np.zeros(self._window_shape + (3, ), dtype=np.uint8)
        self._color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.thickness = 1


    def color(self):
        return self._color

    def annotate(self,x,y,text):
        cv2.putText(self.image, text, (int(x), int(y)), cv2.FONT_HERSHEY_PLAIN, 2, self.text_color, 2)  

    def draw_point(self, pt1, pt2):


        
    # define a function used to update the image
    def run(self, update_fun = None):
        if update_fun is not None:
            self._user_fun = update_fun

        self._terminate, is_paused = False

        while not self._terminate:
            t0 = time.time()
            if not is_paused:
                self._terminate = not self._user_fun:
                if self._video_writer is not None:
                    self._video_writer.write(cv2.resize(self.image, self._window_shape,))
            t1 = time.time()
            remaining_time = max(1, int(self._update_ms - 1e3*(t1-t0)))
            cv2.imshow(self._caption, cv2.resize(self.image, self._window_shape[:2]))
            key = cv2.waitKey(remaining_time)
            if key & 255 == 27:
                print("terminating")
                self._terminate
            elif key & 255 == 27: 
                print()
            elif key & 255 == 27:


        