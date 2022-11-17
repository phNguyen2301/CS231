import cv2


def pencil(img, k_size):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Apply GaussianBlur
    blur = cv2.GaussianBlur(gray, (k_size*2+1, k_size*2+1), 0, 0)
    blend = cv2.divide(gray, blur, scale=250.0)
    canvas = cv2.imread("C:\\Users\\nguye\\Downloads\\pencilsketch_bg.jpg")
    width, height = img.shape[:2]
    img_blend = blend.copy()
    if canvas is not None:
        canvas = cv2.resize(canvas, (height, width))
        canvas = cv2.cvtColor(canvas, cv2.COLOR_RGB2GRAY)
        img_blend = cv2.multiply(blend, canvas, scale=1.0 / 256)
    return img_blend
