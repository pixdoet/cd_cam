"""
    detect.py - the file to pipe camera video to 
    the AI modellllllll
"""
import cv2


class Detector:
    def __init__(self):
        self.person_cascade = cv2.CascadeClassifier(
            f"{cv2.data.haarcascades}haarcascade_upperbody.xml"
        )
        self.countCheck = 0

    def compare(self, source):
        """
        detect - compare video source to model
        @param source - video source from opencv
        """
        rects = self.person_cascade.detectMultiScale(
            source,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        return rects
