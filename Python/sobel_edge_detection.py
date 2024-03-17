import cv2
import numpy as np
import os

video = cv2.VideoCapture(0)

while(True):
    ret, frame = video.read()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    sobel_x = cv2.Sobel(frame, cv2.CV_64F, dx=1, dy=0, ksize=3)
    sobel_y = cv2.Sobel(frame, cv2.CV_64F, dx=0, dy=1, ksize=3)
    sobel_xy = cv2.Sobel(frame, cv2.CV_64F, dx=1, dy=1, ksize=5)

    save_img = "/Users/sowmyamgangadhar/Documents/ComputerVision/2D/Assignments/Image_Processing/results/"
    os.makedirs(save_img, exist_ok=True)

    output_path1 = os.path.join(save_img, "sobel_x.jpg")
    output_path2 = os.path.join(save_img, "sobel_y.jpg")
    output_path3 = os.path.join(save_img, "sobel_xy.jpg")
    cv2.imwrite(output_path1, sobel_x)
    cv2.imwrite(output_path2, sobel_y)
    cv2.imwrite(output_path3, sobel_xy)


   

#     cv2.imshow("sobel", sobel_xy)

#     if cv2.waitKey(1)& 0xFF==ord('q'):
#         break
# video.release()
# cv2.destroyAllWindows()