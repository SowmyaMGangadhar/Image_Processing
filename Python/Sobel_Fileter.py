import cv2
import numpy as np

img = cv2.imread("/Users/sowmyamgangadhar/Documents/ComputerVision/2D/Assignments/Image_Processing/dataset/sunflower2.jpg")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#edge detection x direction, cv_64F: data type for output image, 1,0: x direction, ksize: filter size 5x5
sobel_x = cv2.Sobel(grey, cv2.CV_64F, 1, 0,ksize=3)
#edge detection y direction, cv_64F: data type for output image, 0,1: y direction, ksize: filter size 5x5
sobel_y = cv2.Sobel(grey, cv2.CV_64F, 0,1, ksize=3)

magnitude, direction = cv2.cartToPolar(sobel_x, sobel_y, angleInDegrees=True)

sobel = np.hypot(sobel_x, sobel_y)

sobel = (sobel/sobel.max()) 
# cv2.imshow("flower", sobel)
# cv2.imshow("hori", sobel_x)
# cv2.imshow("verti", sobel_y)
# cv2.imshow("magnitude", magnitude)
cv2.imshow("direction", direction)
cv2.waitKey(0)
cv2.destroyAllWindows()