import cv2
import numpy as numpy


face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
frame = cv2.imread('', cv2.IMREAD_GRAYSCALE)
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray, 1.3,5)
    for (x, y, w, h) in faces :
        cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0),2)
        cv2.imshow('just face', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()