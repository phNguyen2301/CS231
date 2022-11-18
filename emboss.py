import cv2
import numpy as np


def kernel_generator(size):
    kernel = np.zeros((size, size), dtype=np.int8)
    for i in range(size):
        for j in range(size):
            if i < j:
                kernel[i][j] = -1
            elif i > j:
                kernel[i][j] = 1
    return kernel


def emboss(img, val, s):
    h, w = img.shape[:2]
    y = np.ones((h, w), dtype=np.uint8)*128
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    kernel = kernel_generator(val)  # generation kernel for bottom left kernel
    kernel = np.rot90(kernel, s)  # switching kernel according to direction
    res = cv2.add(cv2.filter2D(gray, -1, kernel), y)
    return res
