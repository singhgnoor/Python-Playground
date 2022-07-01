import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray
import time

time.sleep(3)


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds
    for i in range(300, 480):
        for j in range(430,580):
            if data[i, j] < 100:
                print("down")
                hit("down")
                return

    for i in range(300, 480):
        for j in range(560, 690):
            if data[i, j] < 100:
                print("up")
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 
    print("Loop Started")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # print(asarray(image))
        #
        # # Draw the rectangle for birds
        # for i in range(300, 480):
        #     for j in range(563, 690):
        #         data[i, j] = 171
        #
        # # # Draw the rectangle for cactus
        # for i in range(300, 480):
        #     for j in range(430, 580):
        #         data[i, j] = 0

        # image.show()
        # break

