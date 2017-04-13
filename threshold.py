import cv2
import numpy as np

cam_index=int(raw_input("Enter Camera Index : "))
cap = cv2.VideoCapture(cam_index)
def nothing(x):
    pass


cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('h1','image',0,255,nothing)
cv2.createTrackbar('s1','image',0,255,nothing)
cv2.createTrackbar('v1','image',0,255,nothing)

cv2.createTrackbar('h2','image',0,255,nothing)
cv2.createTrackbar('s2','image',0,255,nothing)
cv2.createTrackbar('v2','image',0,255,nothing)


while(1):
  _, frame = cap.read()
  frame=cv2.resize(frame,(512,384))
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
