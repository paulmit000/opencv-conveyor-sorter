import cv2
from config import STREAM_URL

def get_camera():
    return cv2.VideoCapture(STREAM_URL)
