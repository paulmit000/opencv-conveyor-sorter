

import cv2
import numpy as np
from config import STREAM_URL, FRAME_WIDTH
from camera import get_camera, detect_red












if __name__ == "__main__":
    print("STREAM_URL: " + STREAM_URL)
    camera = get_camera()
    print("Camera object: " + str(camera))
    print("Camera isOpened: " + str(camera.isOpened()))

    while True:
        ret, frame = camera.read()
        print("camera.read() returned ret=" + str(ret))
        if not ret:
            print("ret is False, breaking")
            break

        # Process the frame (e.g., display it)
        cv2.imshow('Camera Feed', frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        detected, center = detect_red(frame)
        print("detect_red() returned detected=" + str(detected))
        if detected:
            print("Red object detected at center: " + str(center))
            
            """
            if center < FRAME_WIDTH/2:
                send_left()
                

            else:
                send_right()
            """