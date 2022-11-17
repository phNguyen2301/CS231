import cv2
import numpy as np


def sepia(img):

    res = img.copy()
    res = np.array(res, dtype=np.float64)
    res = cv2.transform(
        res,
        np.matrix([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168],
                   [0.272, 0.534, 0.131]]))
    res[np.where(res > 255)] = 255  # clipping values greater than 255 to 255
    res = np.array(res, dtype=np.uint8)
    return res
