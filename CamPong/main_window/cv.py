import cv2

from tools import Tools

cam = cv2.VideoCapture(0)
cv2.namedWindow('mask')
cv2.namedWindow('frame')

while 1:
    ret, frame = cam.read()
    frame = cv2.resize(frame, (320, 240))
    frame = cv2.flip(frame, 1)
    cv2.imshow('frame', frame)
    frame = Tools.createMask(frame)
    cv2.imshow('mask', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()