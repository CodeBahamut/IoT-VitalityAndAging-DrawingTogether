# Line detection in python with OpenCV

## How it works using Hough Transform 
The Hough Transform is a technique used in image processing to detect any shape that can be represented mathematically. It can detect the shape even if it is slightly broken or distorted.
Using the HoughLine transform method, we will see how the Hough transform works for line detection. To use the Houghline method, an edge detection of the specific image is required first. Read the article Edge detection for more information on the technique.

## Basics of Houghline Method
A line is represented as y = mx + c or, in parametric form, as r = xcos + ysin, where r is the perpendicular distance from the origin to the line and is the angle formed by this perpendicular line and horizontal axis measured in counter-clockwise rotation. (The direction depends on how the coordinate system is represented.) OpenCV makes use of this representation).

![](../images/line-detection-triangle.png)


### The Houghline method in action
It first creates a 2D array or accumulator (to hold the values of two parameters), which is initially set to zero.
Let rows represent the r and columns represent the ()theta.
The size of the array is determined by the level of accuracy required. If you want the accuracy of angles to be one degree, you will need 180 columns (Maximum degree for a straight line is 180).
The maximum distance possible for r is the image's diagonal length. Using one pixel accuracy, the number of rows can be the image's diagonal length.

### code example 
```python
# Python program to illustrate HoughLine
# method for line detection
import cv2
import numpy as np
    def get_image_with_lines2(self, image_path):
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        kernel_size = 5
        blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
        low_threshold = 50
        high_threshold = 150
        edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

        rho = 1  # distance resolution in pixels of the Hough grid
        theta = np.pi / 180  # angular resolution in radians of the Hough grid
        threshold = 15  # minimum number of votes (intersections in Hough grid cell)
        min_line_length = 50  # minimum number of pixels making up a line
        max_line_gap = 20  # maximum gap in pixels between connectable line segments
        line_image = np.copy(img) * 0  # creating a blank to draw lines on

        # Run Hough on edge detected image
        # Output "lines" is an array containing endpoints of detected line segments
        lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                                min_line_length, max_line_gap)

        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)
        lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)

        return lines_edges
```

