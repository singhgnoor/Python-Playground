""" This is a part of Gym Plugin and has logic for Arm Flying Exercise"""

import Pose_Detector
import cv2


class StandingFly:
    """
    Link for reference : http://link.image.com

    """
    detector = Pose_Detector.PoseDetector()

    def __init__(self, debug=True):
        self.debug = debug

    def standing_fly(self):
        for landmark in self.detector.generateLandmarksFromCameraFeed():
            if landmark:
                usable_lm = self.detector.getUsableLandmarks(landmark)

                # Here the logic for Standing Fly Starts
            else:
                self.detector.putNoBodyDetected()

            self.detector.putFPS()

            cv2.imshow("ImShowTitle", self.detector.getFrame())
            if cv2.waitKey(1) & 0xFF == ord("q"):
                print("Bye")
                break







if __name__ == '__main__':
    print("This File is not to accessed this way but for some time you can")

    arm = StandingFly()

    arm.standing_fly()



