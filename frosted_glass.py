import numpy as np


def frosted(src, offsets):
    dst = src.copy()
    rows, cols = src.shape[:2]
    for y in range(rows):
        for x in range(cols):
            random_num = np.random.randint(0, offsets)
            dst[y, x] = src[min(y+random_num, rows - 1),
                            min(x + random_num, cols-1)]
    return dst
