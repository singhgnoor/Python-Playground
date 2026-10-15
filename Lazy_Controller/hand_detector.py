""" This File detects hand movements """

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import os
import cv2
import mediapipe as mp
from mediapipe.tasks.python import BaseOptions, vision
from time import time
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import pyautogui
pyautogui.PAUSE = 0


class HandDetector:
    hands = vision.HandLandmarker.create_from_options(vision.HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "hand_landmarker.task")),
        running_mode=vision.RunningMode.VIDEO,
        num_hands=1,
        min_hand_detection_confidence=.9))
    MpHands = vision.HandLandmarksConnections
    draws = vision.drawing_utils
    last_ts = 0

    height, width = (480, 640)

    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m', 'j', 'p', 'g'))
    cam.set(cv2.CC_STAT_HEIGHT, height)
    cam.set(cv2.CC_STAT_WIDTH, width)

    def __init__(self):
        pass

    cTime = 0
    pTime = time()

    VolumeTrack = False

    volume = AudioUtilities.GetSpeakers().EndpointVolume

    PLayPauseTime = time()
    VolumeTime = time()
    PlayNextTime = time()

    def detectHandsFromImage(self, image, imageRGB, draws=True):
        ts = max(int(time() * 1000), self.last_ts + 1)  # VIDEO mode needs strictly increasing timestamps
        self.last_ts = ts
        result = self.hands.detect_for_video(mp.Image(image_format=mp.ImageFormat.SRGB, data=imageRGB), ts)

        landmarkList = []

        if result.hand_landmarks is not None:
            for hand in result.hand_landmarks:
                tempList = []
                for lmID, lm in enumerate(hand):
                    cx, cy = int(lm.x * self.width), int(lm.y * self.height)
                    tempList.append([cx, cy])
                landmarkList.append(tempList)
                if draws:
                    self.draws.draw_landmarks(image, hand, self.MpHands.HAND_CONNECTIONS)

        return landmarkList, image

    def showHandTrackingFromCameraFeed(self, waitKey="q", ImShowTitle="Hand Detection", actions=True):
        while True:
            ret, img = self.cam.read()
            self.cTime = time()
            fps = str(round(1 / (self.cTime - self.pTime)))
            self.pTime = time()
            img = cv2.flip(img, 1)
            cv2.putText(img, fps, (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 3)
            lmList, img = self.detectHandsFromImage(img, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            yield lmList, img
            # cv2.imshow(ImShowTitle, img)

            # if cv2.waitKey(1) & 0xFF == ord(waitKey):
            #     cv2.destroyAllWindows()
            #     break


