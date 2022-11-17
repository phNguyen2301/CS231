import cv2


def cartoon(img, val):
    # edgesss
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 5)
    img_edges = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, val*2+1, 9)

    # color
    img_color = cv2.bilateralFilter(img, 9, 250, 250)

    # cartoon
    img_edges = cv2.cvtColor(img_edges, cv2.COLOR_GRAY2RGB)
    cartoon = cv2.bitwise_and(img_color, img_edges)

    return cartoon
