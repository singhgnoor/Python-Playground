import sys

sys.path.insert(0, "D:\\Jarvis")
import cv2
import mediapipe as mp
from time import time


class PoseDetector:
    """ This detects a body and return landmarks """
    mpPose = mp.solutions.pose
    pose = mpPose.Pose(min_tracking_confidence=0.85, min_detection_confidence=0.85)
    draws = mp.solutions.drawing_utils

    cam = cv2.VideoCapture(0)

    height, width = (480, 640)

    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m', 'j', 'p', 'g'))
    cam.set(cv2.CC_STAT_HEIGHT, height)
    cam.set(cv2.CC_STAT_WIDTH, width)
    pTime = 0

    def __init__(self):
        self.cTime = None

    def detectPoseFromImage(self, image, imageRGB):
        results = self.pose.process(imageRGB)
        pose_landmarks = results.pose_landmarks
        return pose_landmarks

    def showPoseTrackingFromCameraFeed(self, ImShowTitle="Pose Detection", waitKey="q"):
        while True:
            ret, img = self.cam.read()
            img = cv2.flip(img, 1)

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            lm = self.detectPoseFromImage(img, imgRGB)

            if lm:
                self.draws.draw_landmarks(img, lm, self.mpPose.POSE_CONNECTIONS)

            self.cTime = time()
            fps = str(int(1 / (self.cTime - self.pTime)))
            self.pTime = time()

            cv2.putText(img, fps, (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0))

            cv2.imshow(ImShowTitle, img)
            if cv2.waitKey(1) & 0xFF == ord(waitKey):
                print("Bye")
                break


if __name__ == '__main__':
    print("This file is not to be accessed Directly")
