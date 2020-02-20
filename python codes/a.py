#!/usr/bin/python36
print("content-type:text/html")
print("")

import cv2
cam = cv2.VideoCapture(0)
while 1:
    ret,pic = cam.read()
    x=cv2.imshow('pic.png',pic)
    print(x)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cam.release()
