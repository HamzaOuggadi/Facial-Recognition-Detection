import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')

# Default integrated camera set to cap
cap = cv2.VideoCapture(0)

while(True):
    # Capturing frame by frame
    ret, frame = cap.read()

    grayedFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayedFrame, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        print(x, y, w, h)
        # Region of Interest in the frame (Grayed)
        roi_gray = grayedFrame[y:y+h, x:x+w]
        # Region of Interest in the frame (Colored)
        roi_color = frame[y:y+h, x:x+w]
        # Rectangle
        color = (255, 0, 0)
        stroke = 3
        end_width = x + w
        end_height = y + h
        # Adding Rectangle to the frame
        cv2.rectangle(frame, (x, y), (end_width, end_height), color, stroke)

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
