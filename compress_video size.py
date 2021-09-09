import cv2
import numpy as np

cap = cv2.VideoCapture('D:\\SAIKAT\\out.avi')

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter('output1.avi', fourcc,float(24),(640, 480))

while True:
    ret, frame = cap.read()
    if ret == True:
        b = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_CUBIC)
        cv2.imshow('frame',frame)
        out.write(b)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
