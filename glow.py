import cv2
import numpy as np


def glow(img):
    x = np.array(cv2.filter2D(
        img, -1, np.array([[1.0,  2.0,  1.0], [0.0,  0.0,  0.0], [-1.0, -2.0, -1.0]])), dtype=np.uint32)
    y = np.array(cv2.filter2D(
        img, -1, np.array([[1.0,  2.0,  1.0], [0.0,  0.0,  0.0], [-1.0, -2.0, -1.0]]).T), dtype=np.uint32)
    xy = np.sqrt(x**2 + y**2)
    xy = xy / (np.max(xy)/255.0)
    xy = np.array(xy, dtype=np.uint8)
    return xy
