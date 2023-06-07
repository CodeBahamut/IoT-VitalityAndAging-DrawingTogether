# How to detect a certain colour using Opencv

Firstly, analyzing a basic but important tool for identifying colors through a mask. We’re going to see in this video
how to detect colors through HSV Color space on Opencv with Python.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Q0IPYlIK-4A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

HSV corresponds to:
Hue is the color
Saturation is the greyness
Value is the brightness

Understanding the concepts of balancing these three elements allows us to implement a basic color-based object
recognition system. Here blow is how to make a mask in a few simple steps to balance the recognition of our object in
real-time.
We import the Opencv and Numpy libraries, then load the cap to get the webcam frames. Following that, we begin a while
loop in which we obtain the frames and perform the detection.

```python
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

Within the while loop, we define the HSV ranges (low red, high red), create the mask, and display only the red objects.

```python
    # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
```

Same for the other colors:

```python
    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)
```

We finally show the result:

```python
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    cv2.imshow("Result", result)
    key = cv2.waitKey(1)
    if key == 27:
        break
```

