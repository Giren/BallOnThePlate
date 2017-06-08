import cv2
import numpy as np

points = []

def doCalibration(cap):
    while(1):
        _, frame = cap.read()
        frame=cv2.resize(frame,(600,480))
        cv2.imshow('calibration',frame)
        cv2.setMouseCallback('calibration',setReferencePoints)
        
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

        if len(points)>=2:
            cv2.rectangle(frame, points[0], points[1], (0, 255, 0), 20)
            cv2.imshow('calibration',frame)

    cv2.destroyAllWindows()



def setReferencePoints(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONUP:
        if len(points)==0:
            points = [(x, y)]
        elif len(points)<2:
            points.append((x, y))
