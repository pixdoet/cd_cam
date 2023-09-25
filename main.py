"""
    receive.py - server code for receiving & parsing

"""

#!/usr/bin/env python3

import cv2
import sys


faceCascade = cv2.CascadeClassifier(
    f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml"
)

video_capture = cv2.VideoCapture(1)

#video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)
#video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
h = 640#video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
w =80#video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)

while True:
    # Capture frame-by-frame
    ret, frames = video_capture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE,
    )
    # Draw a rectangle around the faces
    for x, y, w, h in faces:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frames,
            "Person",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )
        print(f"x: {x}; y: {y}")
        cv2.putText(
            frames,
            f"Count: {len(faces)}",
            (50,680),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            3
        )
        if len(faces) > 3:
            print("Crowd detected!")
            cv2.putText(
                frames,
                "Crowd Detected!",
                (50,580),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                3
            )
    # Display the resulting frame
    cv2.imshow(
        f"Lapsap | Press Q to quit",
        frames,
    )
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
