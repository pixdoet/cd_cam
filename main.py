"""
receive.py - server code for receiving & parsing

"""

#!/usr/bin/env python3

import cv2
import getopt, sys

# need to set default height b4 args...
h = 640
w = 80
usefix = False
camera = 2
crowdSize = 1

# cli arguments
argumentList = sys.argv[1:]
options = "hwfcs:"
long_options = ["height", "width", "usefix", "camera", "size"]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # checking each argument
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--height"):
            h = currentValue
        elif currentArgument in ("-w", "--width"):
            w = currentValue
        elif currentArgument in ("-f", "--usefix"):
            if currentValue:
                usefix = True
        elif currentArgument in ("-c", "--camera"):
            camera = currentValue
        elif currentArgument in ("-s", "--size"):
            crowdSize = int(currentValue)

except getopt.error as e:
    print(e)


# import face cascade
faceCascade = cv2.CascadeClassifier(
    f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml"
)

video_capture = cv2.VideoCapture(camera)

# can't remember what this is for, probably for older opencv versions?
if usefix:
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
    video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)

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
            frames, "Person", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
        )
        print(f"x: {x}; y: {y}")
        cv2.putText(
            frames,
            f"Count: {len(faces)}",
            (50, 680),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            3,
        )

        # crowd detected!
        if len(faces) > crowdSize:
            print("Crowd detected!")
            cv2.putText(
                frames,
                "Crowd Detected!",
                (50, 580),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                3,
            )
    # Display the resulting frame
    cv2.imshow(
        f"DetectCrowd | CrowdSize {crowdSize} | Press Q to quit",
        frames,
    )
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
