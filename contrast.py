import cv2
import numpy as np


def contrast(img, factor):
    I = img.copy()

    beta = (1 - factor) * 30
    I = cv2.convertScaleAbs(I, factor=factor, beta=beta)
    return I
