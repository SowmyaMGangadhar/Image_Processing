import cv2
import numpy as np

# img = cv2.imread("/Users/sowmyamgangadhar/Documents/ComputerVision/2D/Assignments/Image_Processing/dataset/sunflower2.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
# # img = cv2.GaussianBlur(img,(15,15),1)
# ce = cv2.Canny(img, 100, 100)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 100, 130)    
    cv2.imshow("canny_edge", canny)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()