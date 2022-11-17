import new_pencil as npe
import cv2

img = cv2.imread('test_image/1.jpg', 0)
pen_tex = './pencils/pencil0.jpg'

test = npe.gen_pencil_drawing(img, kernel_size=17, stroke_width=0, num_of_directions=8, smooth_kernel='gauss',
                              gradient_method=0, rgb=False, w_group=2, pencil_texture_path=pen_tex, stroke_darkness=2, tone_darkness=1.5)

cv2.imshow('test', test)
cv2.imshow('o', img)
cv2.waitKey()
