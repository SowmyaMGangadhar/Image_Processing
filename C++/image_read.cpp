#include <opencv2/opencv.hpp> 
#include<iostream>

using namespace cv;
using namespace std;

int main(){

    // read image
    Mat image_read = imread("/Users/sowmyamgangadhar/Documents/ComputerVision/2D/Assignments/Image_Processing/dataset/cat1.jpg");

    if(image_read.empty()){
        cout<<"image not found"<<endl;
        return -1;
    }

    namedWindow("Image", WINDOW_NORMAL); // Create a window
    imshow("Image", image_read); // Display the image
    waitKey(0); // Wait for any key press

    return 0;

}