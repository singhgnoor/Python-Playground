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

    latest_frame = None

    def __init__(self):
        self.cTime = None

    def detectPoseFromImage(self, image, imageRGB):
        results = self.pose.process(imageRGB)
        pose_landmarks = results.pose_landmarks
        return pose_landmarks

    def showPoseTrackingFromCameraFeed(self, ImShowTitle="Pose Detection", waitKey="q", draws=False):
        while True:
            ret, img = self.cam.read()
            img = cv2.flip(img, 1)

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            lm = self.detectPoseFromImage(img, imgRGB)

            self.cTime = time()
            fps = str(int(1 / (self.cTime - self.pTime)))
            self.pTime = time()

            cv2.putText(img, fps, (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0))

            cv2.imshow(ImShowTitle, img)
            if cv2.waitKey(1) & 0xFF == ord(waitKey):
                print("Bye")
                break

    def generateLandmarksFromCameraFeed(self):
        while True:
            ret, img = self.cam.read()
            img = cv2.flip(img, 1)

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            lm = self.detectPoseFromImage(img, imgRGB)

            self.latest_frame = img

            yield lm

    def getUsableLandmarks(self, mp_landmarks):
        """
        usable_landmarks :
        Format: [[x, y, depth, visibility], [x, y, depth, visibility], ..]

        raw eg :
            x: 0.44502395391464233
            y: 1.3300063610076904
            z: -0.049073003232479095
            visibility: 0.005143297370523214

        """
        usable_landmarks = []
        for lm in mp_landmarks.landmark[11::]:
            usable_landmarks.append([round(lm.x * self.width), round(lm.y * self.height), lm.z, lm.visibility])
        return usable_landmarks

    def putNoBodyDetected(self, frame=latest_frame):
        cv2.putText(self.latest_frame, "No Body Detected", (40, round(self.height / 2)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))

    def putFPS(self):
        try:
            self.cTime = time()
            fps = str(int(1 / (self.cTime - self.pTime)))
            self.pTime = time()
        except ZeroDivisionError:
            fps = "Bahut Zada"
        cv2.putText(self.latest_frame, fps, (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0))

    def getFrame(self):
        return self.latest_frame



if __name__ == '__main__':
    print("This file is not to be accessed Directly")
