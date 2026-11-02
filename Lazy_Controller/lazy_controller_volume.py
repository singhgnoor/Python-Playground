""" This file will help me to use laptop from bed """

from hand_detector import HandDetector
import cv2
from time import time
import math
import pyautogui

pyautogui.PAUSE = 0

handDetect = HandDetector()

move_disable_time = time()
move_enable = False

for (lm, img) in (handDetect.showHandTrackingFromCameraFeed()):


    if lm:
        indexFingerUp = False
        MiddleFingerUp = False
        RingFingerUp = False
        PinkyFingerUp = False
        ThumbUp = False
        RightHand = False
        LeftHand = False

        indexOfHand = 0

        if lm[indexOfHand][8][1] < lm[indexOfHand][6][1]: indexFingerUp = True

        if lm[indexOfHand][12][1] < lm[indexOfHand][10][1]: MiddleFingerUp = True

        if lm[indexOfHand][16][1] < lm[indexOfHand][14][1]: RingFingerUp = True

        if lm[indexOfHand][20][1] < lm[indexOfHand][18][1]: PinkyFingerUp = True

        if (lm[indexOfHand][0][0] + 20) > lm[indexOfHand][2][0]:
            RightHand = True
            cv2.putText(img, "Right", (10, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 3)
        else:
            LeftHand = True
            cv2.putText(img, "Left", (10, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 3)

        # Volume: only index and thumb out (index tip above its knuckle, so a fist doesn't count)
        if not MiddleFingerUp and not RingFingerUp and not PinkyFingerUp and lm[indexOfHand][8][1] < lm[indexOfHand][5][1]:
            thumbTip = tuple(lm[indexOfHand][4])
            indexTip = tuple(lm[indexOfHand][8])
            midPoint = ((thumbTip[0] + indexTip[0]) // 2, (thumbTip[1] + indexTip[1]) // 2)

            handSize = math.dist(lm[indexOfHand][0], lm[indexOfHand][5])
            extension = min(math.dist(thumbTip, indexTip) / (handSize * 1.5), 1)  # 1.5 x hand size = fully extended

            if extension < 0.1:
                vol = 0
                colour = (0, 0, 0)
            else:
                vol = (extension - 0.1) / 0.9
                colour = (int(255 * (1 - vol)), 0, int(255 * vol))  # blue -> red

            handDetect.volume.SetMasterVolumeLevelScalar(vol, None)
            cv2.line(img, thumbTip, indexTip, colour, 3)
            cv2.circle(img, midPoint, 10, colour, cv2.FILLED)

        if not indexFingerUp and MiddleFingerUp and not RingFingerUp and not PinkyFingerUp:
            print("Bye")
            break

        if move_enable:
            # print(f"wrist = {lm[indexOfHand][0]}, index_joint = {lm[indexOfHand][5]}")
            if RightHand and indexFingerUp and MiddleFingerUp and RingFingerUp:
                if lm[indexOfHand][0][0] - 20 > lm[indexOfHand][13][0]:
                    cv2.putText(img, "Previous", (10, 400), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 3)
                    move_enable = False
                    move_disable_time = time()
                    pyautogui.press("prevtrack", presses=2, interval=0.1)

                if lm[indexOfHand][0][0] + 20 < lm[indexOfHand][5][0]:
                    cv2.putText(img, "Next", (10, 400), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 3)
                    move_enable = False
                    move_disable_time = time()
                    pyautogui.press("nexttrack")

        if not move_enable and not indexFingerUp and not MiddleFingerUp and not RingFingerUp and not PinkyFingerUp:
            if (time() - move_disable_time) > 1.5:
                move_enable = True
                cv2.putText(img, "Enabled", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 3)

    cv2.imshow("Hand", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

