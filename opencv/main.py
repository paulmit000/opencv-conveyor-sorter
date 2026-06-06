

import cv2
import numpy as np
import urllib.request
from config import CAPTURE_URL, FRAME_WIDTH
from camera import get_camera, detect_red, detect_blue


def fetch_frame_from_snapshot(url):
    response = urllib.request.urlopen(url, timeout=2)
    img_bytes = response.read()
    img_np = np.array(bytearray(img_bytes), dtype=np.uint8)
    return cv2.imdecode(img_np, cv2.IMREAD_COLOR)


if __name__ == "__main__":
    stream_url = get_camera()
    print("Stream URL: " + stream_url)

    capture = cv2.VideoCapture(stream_url)
    use_snapshot_fallback = not capture.isOpened()

    if use_snapshot_fallback:
        print(f"Failed to open MJPEG stream. Falling back to snapshot URL: {CAPTURE_URL}")

    while True:
        try:
            if use_snapshot_fallback:
                frame = fetch_frame_from_snapshot(CAPTURE_URL)
            else:
                ret, frame = capture.read()
                if not ret:
                    print("Stream read failed, retrying...")
                    continue

            if frame is None:
                print("Failed to decode frame")
                continue

            if FRAME_WIDTH and frame.shape[1] > FRAME_WIDTH:
                height = int(frame.shape[0] * FRAME_WIDTH / frame.shape[1])
                frame = cv2.resize(frame, (FRAME_WIDTH, height), interpolation=cv2.INTER_LINEAR)

            cv2.imshow('Camera Feed', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            red_detected, red_center = detect_red(frame)
            blue_detected, blue_center = detect_blue(frame)

            if red_detected:
                print("Red object detected at center: " + str(red_center))
            if blue_detected:
                print("Blue object detected at center: " + str(blue_center))

        except Exception as e:
            print(f"Skipped frame: {e}")
            continue

    if not use_snapshot_fallback:
        capture.release()
    cv2.destroyAllWindows()
    print("Closed cleanly.")