import speech_recognition as sr  # pip install speechRecognition
import datetime
import os
from time import sleep
import random

# it will genrate random string for giving random name to different file
def GenRanName():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    strYear = datetime.datetime.today().strftime('%Y-%m-%d')
    strYear = strYear.replace("-", "")
    strTime = strTime.replace(":", "")
    return(f"{strYear}_{strTime}")

# It takes microphone input from the user and returns string output
def takeCommand():
    """ It takes microphone input from the user and returns string output """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 50
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        if 'type this' in query:
            query = ""
            query = input("Type please: ")

    except Exception as e:
        print("Say that again please...")
        return ""
    return query

def addContent():
    print("Please speak name of the file")
    name = takeCommand()
    if name == "":
        print("Name not Given, Genrating Random Name for the File")
        name = "TXT_"
        name += GenRanName()
    os.chdir(r'G:\\Notes genrated By Python\\')

    if os.path.exists(f"{name}.txt"):
        file = open(f"{name}.txt", "a")
        file.write("\n")
    else:
        file = open(f"{name}.txt", "x")

    print("Please speak the content")
    content = takeCommand()
    if content == "":
        print("Skiping as the nothing is said")
    file.write(content)
    file.close()

    print('Content added to the file.')
    print("Need to open the file")
    
    op = takeCommand().lower()
    if "yes" in op or "sure" in op or 'open' in op:
        try:
            print("Opening file")
            os.startfile(f"G:\\Notes genrated By Python\\{name}.txt") 
        except:
            print("Cannot Open The file")

    return
if __name__ == "__main__":
    addContent()
    sleep(10)