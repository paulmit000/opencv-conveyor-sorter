

import cv2
from config import STREAM_URL, FRAME_WIDTH
from camera import get_camera

if __name__ == "__main__":
    camera = get_camera()

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Process the frame (e.g., display it)
        cv2.imshow('Camera Feed', frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        detected, center = detect_red(frame)
        if detected:
            print("Red object detected at center: " + str(center))
            
            """
            if center < FRAME_WIDTH/2:
                send_left()
                

            else:
                send_right()
            """