# macOS 14.6
# Python 3.6
# openCV 3.4.2

# You should use original terminal to execute it.

import cv2

cv2.namedWindow("2018 MacBook Pro Preview")
vc = cv2.VideoCapture(0)

rval, frame = vc.read()

while True:

    if frame is not None:
        cv2.imshow("2018 MacBook Pro Preview", frame)
    rval, frame = vc.read()

    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        break
