import cv2
import uuid
import numpy as np

video = cv2.VideoCapture(0)

while video.isOpened():
    ret, frame = video.read()

    if ret:
        cv2.imshow(winname= "frame", mat = np.array(frame))
        if(cv2.waitKey(1) == ord('a')):
            cv2.imwrite(f"Anchor/{uuid.uuid1()}.png", frame)

        if(cv2.waitKey(1) == ord('p')):
            cv2.imwrite(f"images_mine/{uuid.uuid1()}.png", frame)
        
        if(cv2.waitKey(1) == ord('q')):
            cv2.destroyAllWindows()

