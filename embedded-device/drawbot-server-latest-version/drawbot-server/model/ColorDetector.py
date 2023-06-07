import string

import cv2
import numpy as np
# import pandas as pd


class ColorDetector:
    def __init__(self) -> None:
        self.upper_blue = None
        print("color detector is being initialized")
        self.setUp()

    def setUp(self):
        # BGR
        self.lower_red = np.array([0, 0, 150], dtype="uint8")
        self.upper_red = np.array([100, 100, 255], dtype="uint8")
  
        self.lower_green = np.array([0, 100, 0], dtype="uint8")
        self.upper_green = np.array([100, 255, 100], dtype="uint8")
        
        self.lower_blue = np.array([100, 0, 0], dtype="uint8")
        self.upper_blue = np.array([255, 100, 100], dtype="uint8")

    def detect_color(self, image) -> string:
        return self._get_prominent_color(image)

    def _get_prominent_color(self, image):
        COLOUR_MIN_COUNT = 10000

        red_mask = cv2.inRange(image, self.lower_red, self.upper_red)
        green_mask = cv2.inRange(image, self.lower_green, self.upper_green)
        blue_mask = cv2.inRange(image, self.lower_blue, self.upper_blue)

        red_count = np.sum(np.nonzero(red_mask))
        green_count = np.sum(np.nonzero(green_mask))
        blue_count = np.sum(np.nonzero(blue_mask))

        red_average = cv2.mean(red_mask)[0]
        green_average = cv2.mean(green_mask)[0]
        blue_average = cv2.mean(blue_mask)[0]

        # Debugging purposes
        #         print("red ", red_count , " " , red_average)
        #         print("green ", green_count , " " , green_average)
        #         print("blue ", blue_count , " " , blue_average)

        array = [red_count, green_count, blue_count]

        highestIndex = None
        highest = COLOUR_MIN_COUNT
        for i in range(3):
            if array[i] > highest:
                highest = array[i]
                highestIndex = i

        if highestIndex == 0:
            return "Red"
        elif highestIndex == 1:
            return "Green"
        elif highestIndex == 2:
            return "Blue"

        return "None"
