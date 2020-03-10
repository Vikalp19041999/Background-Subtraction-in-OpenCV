import numpy as np
import cv2
from cv2 import *

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=20, detectShadows=True)

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30)
    if k==27:
        break
        
cap.release()
cv2.destroyAllWindows()