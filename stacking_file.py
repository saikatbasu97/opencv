import cv2
import numpy as np
vid1='Original_sample.mp4'
cap1 = cv2.VideoCapture(vid1)
cap2 = cv2.VideoCapture('Sample.mp4')

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter('new2.avi', fourcc,float(20),(620,480))
while cap1.isOpened() or cap2.isOpened():

    okay1, frame1 = cap1.read()
    okay2, frame2 = cap2.read()
    stack = np.concatenate((frame1, frame2), axis=1)
    b = cv2.resize(stack, (620,480), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('frame', stack)
    print(stack.shape[:2])
    out.write(b)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()