import cv2
import numpy as np
import urllib.request
from config import STREAM_URL

def get_camera():
    # Return the stream URL instead of a VideoCapture object
    return STREAM_URL

def detect_color(frame, lower, upper):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    M = cv2.moments(mask)
    if M["m00"] == 0:
        return False, None
    return True, int(M["m10"] / M["m00"])


def detect_red(frame):
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red1, upper_red1)
    mask |= cv2.inRange(hsv, lower_red2, upper_red2)

    M = cv2.moments(mask)
    if M["m00"] == 0:
        return False, None
    return True, int(M["m10"] / M["m00"])


def detect_blue(frame):
    lower_blue = np.array([90, 100, 100])
    upper_blue = np.array([130, 255, 255])
    return detect_color(frame, lower_blue, upper_blue)
