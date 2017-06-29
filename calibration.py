import cv2
import numpy as np

points = []


def doCalibration(cap):
    global points
    cv2.namedWindow('calibration')
    cv2.setMouseCallback('calibration',setReferencePoints)
    while(1):
        _, calibrationFrame = cap.read()
        calibrationFrame=cv2.resize(calibrationFrame,(600,480))
        
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        
        if k == 13:
            points = []

        if len(points)>=2:
            cv2.rectangle(calibrationFrame, points[0], points[1], (0, 255, 0), 20)

        cv2.imshow('calibration',calibrationFrame)

    cv2.destroyAllWindows()



def setReferencePoints(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONUP:
        if len(points)==0:
            points = [(x, y)]
        elif len(points)<2:
            points.append((x, y))

