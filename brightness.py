import cv2
import numpy as np


def brightness(img, factor):

    I = img.copy()
    I = cv2.convertScaleAbs(I, alpha=factor, beta=0)
    return I
