import string

import cv2
import numpy as np
import pandas as pd
class ColorDetector:
    def __init__(self) -> None:
        self.upper_blue = None
        print("color detector is being initialized")
        self.setUp()

    def setUp(self):
        index = ["color", "color_name", "hex", "R", "G", "B"]
        self.csv = pd.read_csv('primary-colors.csv', names=index, header=None)
        # self.lower_red = np.array([136, 87, 111], dtype="uint8")
        # self.upper_red = np.array([180, 255, 255], dtype="uint8")
        #
        # self.lower_green = np.array([25, 52, 72], dtype="uint8")
        # self.upper_green = np.array([102, 255, 255], dtype="uint8")
        #
        # self.lower_blue = np.array([94, 80, 2], dtype="uint8")
        # self.upper_blue = np.array([120, 255, 255], dtype="uint8")


    # def detectColor(self, image_path) -> string:
    #     image = cv2.imread(image_path)
    #     return self._get_prominent_color(image)

    # to show the detected part of the image
    #   detected_output = cv2.bitwise_and(image, image, mask=mask)
    #   cv2.imshow("red color detection", detected_output)
    #   cv2.waitKey(0)

    # def _get_prominent_color(self, image):
    #     red_mask = cv2.inRange(image, self.lower_red, self.upper_red)
    #     green_mask = cv2.inRange(image, self.lower_green, self.upper_green)
    #     blue_mask = cv2.inRange(image, self.lower_blue, self.upper_blue)
    #
    #     red_count = np.sum(np.nonzero(red_mask))
    #     green_count = np.sum(np.nonzero(green_mask))
    #     blue_count = np.sum(np.nonzero(blue_mask))
    #
    #     red_average = cv2.mean(red_mask)[0]
    #     green_average = cv2.mean(green_mask)[0]
    #     blue_average = cv2.mean(blue_mask)[0]
    #
    #     print("red ", red_count , " " , red_average)
    #     print("green ", green_count , " " , green_average)
    #     print("blue ", blue_count , " " , blue_average)
    #     if red_count > 0:
    #         return "Red"
    #     elif green_count > 0:
    #         return "Green"
    #     elif blue_count > 0:
    #         return "Blue"
    #     return "No color detected"


    def get_color_name(self, image):
        global b,g,r
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                b, g, r = image[x, y]
                b = int(b)
                g = int(g)
                r = int(r)
                color_name = self._get_name_from_csv(r, g, b)
                [name ,is_primary_color] = self._check_color(color_name)
                if (is_primary_color):
                    return name
        return ""

    def unique_count_app(self,a):
        colors, count = np.unique(a.reshape(-1, a.shape[-1]), axis=0, return_counts=True)
        return colors[count.argmax()]

    def _get_name_from_csv(self, R, G, B):
        minimum = 10000
        for i in range(len(self.csv)):
            d = abs(R - int(self.csv.loc[i, "R"])) + abs(G - int(self.csv.loc[i, "G"])) + abs(B - int(self.csv.loc[i, "B"]))
            if (d <= minimum):
                minimum = d
                cname = self.csv.loc[i, "color_name"]
        return cname

    def load_csv(self):
        for i in range(len(self.csv)):
                row = self.csv.loc[i]
                print(row +"\n")

    def _check_color(self, color_name)-> [string, bool]:
        if "Blue" in color_name:
            return "Blue", True
        elif "Red" in color_name:
            return "Red", True
        elif "Green" in color_name:
            return "Green", True
        elif "Yellow" in color_name:
            return "Yellow", True
        elif "Orange" in color_name:
            return "Orange", True
        elif "Pink" in color_name:
            return "Pink", True

        return "", False
