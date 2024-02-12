import cv2
import numpy as np

video = cv2.VideoCapture(0)

while(True):
    ret, frame = video.read()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    sobel_x = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=3)

    sobel = np.hypot(sobel_x, sobel_y)
    sobel = (sobel/sobel.max())

    cv2.imshow("sobel", sobel)

    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows()