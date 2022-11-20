import contrast
import brightness
import sepia
import emboss
import frosted_glass
import glow
import pencil
import cartoon
import cv2
import time
# webcam

# cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture("vid.mp4")
fps= int(cap.get(cv2.CAP_PROP_FPS))
while(cap.isOpened()):
    #Đọc video
    ret, frame = cap.read()
    time.sleep(1/fps)
    cv2.imshow('frame',frame)

    # pencil_frame = pencil.pencil(frame, 10) 
    # cv2.imshow('frame1',pencil_frame)

    # brightness_frame = brightness.brightness(frame, -80)
    # cv2.imshow('frame2',brightness_frame)

    # emboss_frame = emboss.emboss(frame, 4, 0)
    # cv2.imshow('frame3',emboss_frame)

    # glow_frame = glow.glow(frame)
    # cv2.imshow('frame4',glow_frame)

    # sepia_frame = cv2.cvtColor( sepia.sepia(frame) , cv2.COLOR_RGB2BGR)
    # cv2.imshow('frame5',sepia_frame)

    cartoon_frame = cartoon.cartoon(frame,val=9)
    cv2.imshow('fram6',cartoon_frame)

    contrast_frame = contrast.contrast(frame, 1.5)
    cv2.imshow('fram7',contrast_frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break