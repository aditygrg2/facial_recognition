import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read() 

    if ret:
        gray = cv2.cvtColor(src = frame, code = cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(image = gray, scaleFactor=2, minNeighbors=1)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow(winname = 'Face Detection', mat = np.array(frame))
        if(cv2.waitKey(1) == ord('a')):
            cv2.destroyAllWindows()