import cv2
import numpy as np
import mouseclick

def doCalibration(cap):
    while(1):
        _, frame = cap.read()
        frame=cv2.resize(frame,(600,480))
        cv2.imshow('calibration',frame)
        cv2.setMouseCallback('calibration',mouseclick.setReferencePoints)
        
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
