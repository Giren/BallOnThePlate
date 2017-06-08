import cv2
import numpy as np
import RangeConfig
import calibration

cam_index=int(raw_input("Enter Camera Index : "))
cap = cv2.VideoCapture(cam_index)

calibration.doCalibration(cap)

def persist_values(x):
    config.set_low_range(h1, s1, v1)
    config.set_high_range(h2, s2, v2)

config = RangeConfig.RangeConfig("./config.ini")
h1 = config.lowRange[0]
s1 = config.lowRange[1]
v1 = config.lowRange[2]

h2 = config.highRange[0]
s2 = config.highRange[1]
v2 = config.highRange[2]

cv2.namedWindow('image',flags=cv2.WINDOW_NORMAL)
# create trackbars for color change
cv2.createTrackbar('h1','image', h1, 255, persist_values)
cv2.createTrackbar('s1','image', s1, 255, persist_values)
cv2.createTrackbar('v1','image', v1, 255, persist_values)

cv2.createTrackbar('h2','image', h2, 255, persist_values)
cv2.createTrackbar('s2','image', s2, 255, persist_values)
cv2.createTrackbar('v2','image', v2, 255, persist_values)

while(1):
  _, frame = cap.read()
  frame=cv2.resize(frame,(600,480))
  frame=cv2.medianBlur(frame, 5)
  # Convert BGR to HSV
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  h1 = cv2.getTrackbarPos('h1','image')
  s1 = cv2.getTrackbarPos('s1','image')
  v1 = cv2.getTrackbarPos('v1','image')

  h2 = cv2.getTrackbarPos('h2','image')
  s2 = cv2.getTrackbarPos('s2','image')
  v2 = cv2.getTrackbarPos('v2','image')

  lower= np.array([h1,s1,v1])
  upper = np.array([h2,s2,v2])
  # Threshold the HSV image to get only blue colors
  mask = cv2.inRange(hsv, lower, upper)

  cv2.imshow('frame',frame)
  cv2.imshow('thresh',mask)

  k = cv2.waitKey(5) & 0xFF
  if k == 27:
    break

cv2.destroyAllWindows()
