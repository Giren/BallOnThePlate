# import the necessary packages
import argparse
import cv2

def setReferencePoints(event, x, y, flags, param):
    # check to see if the left mouse button was released
    if event == cv2.EVENT_LBUTTONUP:
        return [(x, y)]
