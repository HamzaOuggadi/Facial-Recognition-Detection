import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')

# Default integrated camera set to cap
cap = cv2.VideoCapture(0)

while(True):
    # Capturing frame by frame
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
