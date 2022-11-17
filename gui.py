from os import startfile
from numpy.lib.function_base import copy
from sepia import sepia
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import cv2
from PIL import ImageTk, Image
import contrast
import brightness
import sepia
import emboss
import frosted_glass
import glow
import pencil
import cartoon

SIZE = 700


def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized


def importImg(label):
    global img_input
    global current
    current = None
    filetypes = (
        ('all files', '*.*'),
        ('png files', '*.png'),
        ('jpg files', '*.jpg')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='./pics',
        filetypes=filetypes
    )

    if filename:
        showinfo(
            title='Import Image',
            message='Import Succeed'
        )
    else:
        showinfo(
            title='Error!',
            message='Please import again'
        )
        return

    img_input = cv2.imread(filename)
    img_input = cv2.cvtColor(img_input, cv2.COLOR_BGR2RGB)
    img_input_display = img_input.copy()

    global h, w
    h, w = img_input_display.shape[:2]
    if h > w:
        if h > SIZE:
            img_input_display = image_resize(img_input_display, height=SIZE)
    else:
        if w > SIZE:
            img_input_display = image_resize(img_input, width=SIZE)
    h, w = img_input_display.shape[:2]

    img_1 = ImageTk.PhotoImage(image=Image.fromarray(img_input_display))

    label.config(image=img_1)
    label.image = img_1
    label.grid(row=1, column=1)


def disable_slider(next):
    global current
    if current == 'brightness':
        brightness_slider.place(x=-100, y=-100)
    if current == 'contrast':
        contrast_slider.place(x=-100, y=-100)
    if current == 'cartoon':
        cartoon_slider.place(x=-100, y=-100)
    if current == 'emboss':
        emboss_slider_1.place(x=-100, y=-100)
        emboss_slider_2.place(x=-100, y=-100)
    if current == 'pencil':
        pencil_slider.place(x=-100, y=-100)
    current = next


def enable_slider():
    if current == 'brightness':
        brightness_slider.place(x=320, y=705)
    if current == 'contrast':
        contrast_slider.place(x=320, y=705)
    if current == 'cartoon':
        cartoon_slider.place(x=320, y=705)
    if current == 'emboss':
        emboss_slider_1.place(x=320, y=705)
        emboss_slider_2.place(x=740, y=705)
    if current == 'pencil':
        pencil_slider.place(x=320, y=705)


def previewImg(label, filter=None, val=0, val2=0):
    global img_output
    img_output = img_input.copy()
    if filter == 'brightness':
        img_output = brightness.brightness(img_input, val)

    elif filter == 'contrast':
        img_output == contrast.contrast(img_input, val, val2)

    elif filter == 'cartoon':
        img_output = cartoon.cartoon(img_input, val)

    elif filter == 'emboss':
        img_output = emboss.emboss(img_input, val, val2)

    elif filter == 'frosted_glass':
        img_output = frosted_glass.frosted(img_input, val)

    elif filter == 'pencil':
        img_output = pencil.pencil(img_input, val)

    elif filter == 'sepia':
        img_output = sepia.sepia(img_input)
    elif filter == 'glowing_edge':
        img_output = glow.glow(img_input)

    img_output_display = cv2.resize(img_output, (w, h))
    img_2 = ImageTk.PhotoImage(image=Image.fromarray(img_output_display))
    label.config(image=img_2)
    label.image = img_2
    label.grid(row=1, column=2)
    disable_slider(filter)
    disable_slider(filter)
    enable_slider()


def exportImg(img):
    defaultextension = '.png'
    filename = fd.asksaveasfile(mode='w', defaultextension=defaultextension)
    if not filename:
        return
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(filename.name, img)


current = None
window = Tk()
window.geometry('1550x763')
window.resizable(0, 0)
window.title('Some Photoshop filters')

my_label = Button(window)

import_button = Button(window, text='Import image', bg='black', fg='white')
import_button.config(command=lambda: importImg(my_label))
import_button.config(height=2, width=15)
import_button.place(x=25, y=705)

# FILTER_BUTTONS
my_label_2 = Button(window)

brightness_button = Button(window, text='Brightness', bg='black', fg='white')
brightness_button.config(command=lambda: previewImg(
    my_label_2, filter='brightness', val=1))
brightness_button.config(height=2, width=15)
brightness_button.place(x=1420, y=45)

contrast_button = Button(window, text='Contrast', bg='black', fg='white')
contrast_button.config(command=lambda: previewImg(
    my_label_2, filter='contrast', val=0.5))
contrast_button.config(height=2, width=15)
contrast_button.place(x=1420, y=125)

frosted_glass_button = Button(window, text='Frosted', bg='black', fg='white')
frosted_glass_button.config(command=lambda: previewImg(
    my_label_2, filter='frosted_glass', val=8))
frosted_glass_button.config(height=2, width=15)
frosted_glass_button.place(x=1420, y=205)

emboss_button = Button(window, text='Emboss', bg='black', fg='white')
emboss_button.config(command=lambda: previewImg(
    my_label_2, filter='emboss', val=2, val2=0))
emboss_button.config(height=2, width=15)
emboss_button.place(x=1420, y=285)

sepia_button = Button(window, text='Sepia', bg='black', fg='white')
sepia_button.config(command=lambda: previewImg(my_label_2, filter='sepia'))
sepia_button.config(height=2, width=15)
sepia_button.place(x=1420, y=365)

cartoon_button = Button(window, text='Cartoon', bg='black', fg='white')
cartoon_button.config(command=lambda: previewImg(
    my_label_2, filter='cartoon', val=1))
cartoon_button.config(height=2, width=15)
cartoon_button.place(x=1420, y=445)

pencil_button = Button(window, text='Pencil', bg='black', fg='white')
pencil_button.config(command=lambda: previewImg(
    my_label_2, filter='pencil', val=8))
pencil_button.config(height=2, width=15)
pencil_button.place(x=1420, y=525)

glowing_button = Button(window, text='Glowing', bg='black', fg='white')
glowing_button.config(command=lambda: previewImg(
    my_label_2, filter='glowing_edge'))
glowing_button.config(height=2, width=15)
glowing_button.place(x=1420, y=605)

export_button = Button(window, text='Export image', bg='black', fg='white')
export_button.config(command=lambda: exportImg(img_output))
export_button.config(height=2, width=15)
export_button.place(x=1420, y=705)

# SLIDER
pencil_slider = Scale(window, from_=1, to=30, length=800, orient=HORIZONTAL)
pencil_slider.config(command=lambda val: previewImg(
    my_label_2, filter='pencil', val=int(val)))
# pencil_slider.place(x = 320, y = 705)

brightness_slider = Scale(window, from_=0, to=3.0,
                          length=800, resolution=0.1, orient=HORIZONTAL)
brightness_slider.set(1.0)
brightness_slider.config(command=lambda val: previewImg(
    my_label_2, filter='brightness', val=float(val)))
# brightness_slider.place(x = 320, y = 705)

contrast_slider = Scale(window, from_=0, to=3.0,
                        resolution=0.1, length=800, orient=HORIZONTAL)

cartoon_slider = Scale(window, from_=1, to=15, length=800, orient=HORIZONTAL)
cartoon_slider.config(command=lambda val: previewImg(
    my_label_2, filter='cartoon', val=int(val)))


emboss_slider_1 = Scale(window, length=380, from_=2, to=10, orient=HORIZONTAL)
emboss_slider_1.config(command=lambda val: previewImg(
    my_label_2, filter='emboss', val=int(val), val2=int(emboss_slider_2.get()) - 1))
emboss_slider_2 = Scale(window, length=380, from_=1,
                        to=4, tickinterval=1, orient=HORIZONTAL)
emboss_slider_2.config(command=lambda val: previewImg(
    my_label_2, filter='emboss', val=int(emboss_slider_1.get()), val2=int(val) - 1))


window.mainloop()
