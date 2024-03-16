import cv2
import numpy as np
import os

def sobel_filter(img):
    # img = cv2.imread('/Users/sowmyamgangadhar/Documents/ComputerVision/2D/Assignments/Image_Processing/dataset/sunflower1.jpg')
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    sobel_y = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]])
    print(sobel_x, sobel_y)

    [row, col] = np.shape(grey)
    print(row, col)
    sob = np.zeros(shape=(row, col), dtype=np.float64)
    for i in range(row-2):
        for j in range(col-2):
            gx = np.sum(np.multiply(sobel_x, grey[i:i+3, j:j+3]))
            gy = np.sum(np.multiply(sobel_y, grey[i:i+3, j:j+3]))
            # print(gx,gy)
            sob[i+1, j+1] = np.sqrt(gx**2 + gy**2)
    sob = cv2.normalize(sob, None, 0, 255, cv2.NORM_MINMAX)
    sob = sob.astype(np.uint8)

    save_img = "/Users/sowmyamgangadhar/Documents/ComputerVision/2D/Assignments/Image_Processing/results/"
    os.makedirs(save_img, exist_ok=True)

    output_path = os.path.join(save_img, "sobel_scartch.jpg")
    
    cv2.imwrite(output_path, sob)
    cv2.imshow("sobel",sob)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('/Users/sowmyamgangadhar/Documents/ComputerVision/2D/Assignments/Image_Processing/dataset/sunflower1.jpg')
sobel_filter(img)