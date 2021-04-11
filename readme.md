# How it's works
1. First dowload library opencv and numpy 
````
pip install opencv-python
pip install numpy
````
2. Make the program to connect to the webcam
```
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    cv2.imshow('just face', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
`````
3. Download the model for face, that is haarcascade_frontalface_default.xml
4. Write the code to translate the model
````
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
````
5. Load the image in grayscale
````
frame = cv2.imread('', cv2.IMREAD_GRAYSCALE)
````
By changing to gray, the program will be easier to learn

6. Turn the picture to gray color
````
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
````
7. To make a rectangle, use this code
````
    for (x, y, w, h) in faces :
        cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0),2)
````

# Demo
[![Watch the video](https://i.imgur.com/maxresdefault.jpg.png)](https://youtu.be/8zHq6wxWeec)
