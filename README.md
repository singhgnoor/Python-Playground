# Python Playground 🐍

This is where my random Python ideas end up. Some of it is school practice, some of it is me playing around with OpenCV and MediaPipe, and some of it is small tools I wanted for myself. Not everything here is finished, and a few things are just started and left alone.

## What's inside

**Computer vision 📷**

- [Lazy_Controller](Lazy_Controller/): control my laptop from bed with hand gestures. MediaPipe tracks which fingers are up, and `pyautogui` sends next/previous track keys. Volume control via `pycaw` is set up but not wired in yet.
- [Gym](Gym/): the start of a workout tracker. [Pose_Detector.py](Gym/Pose_Detector.py) wraps MediaPipe Pose.
- [Motion detector](Motion%20detector/): OpenCV frame differencing that boxes movement and plays `alert.wav` (Windows only, because it uses `winsound`).
- [Emojify](Emojify/): a Keras CNN for webcam emotion detection. The training code is there, but the dataset isn't included and inference doesn't load the weights properly yet. Experimental.

**Games and automation 🎮**

- [Flappy Bird](Flappy%20Bird/): a Flappy Bird clone in `pygame` with sprites, sounds and `pyttsx3` voice. Probably the most complete thing in here.
- [Chrome Dino Game automation](Chrome%20Dino%20Game%20automation/): reads screen pixels with Pillow and jumps/ducks with `pyautogui`. The coordinates are tuned to my screen.
- [Guess the Number](Guess%20the%20Number/) and [WhatsApp Automation](WhatsApp%20Automation/) (a tiny `pywhatkit` test).

**Small tools 🔧**

- [Instagram Data Analyser](Instagram%20Data%20Analyser/): reads your Instagram data export and lists who doesn't follow you back.
- [Investor](Investor/): monthly investment calculator with a yearly step-up and CSV export.
- [IP_Tracker](IP_Tracker/) (ipapi.co lookup), [Phone Info](Phone%20Info/) (`phonenumbers`), [PassWord Genrator](PassWord%20Genrator/), [Youtube Handler](Youtube%20Handler/) (`pytube`, WIP), [Text From Speech](Text%20From%20Speech/) (dictate notes with `SpeechRecognition`), [Key Logger](Key%20Logger/) (Windows experiment that logs my own keystrokes to `Logs/`).

**Learning bits 📚**

[Math](Math/) (interest, HCF, frequency tables), [Mensuration](Mensuration/), [Calculator](Calculator/), [Factorial_Calculator](Factorial_Calculator/), [Fibonacci_series](Fibonacci_series/), [Data Handling](Data%20Handling/) (pandas CSV basics), [Encoder](Encoder/) (unfinished), [Music_Classifiyer](Music_Classifiyer/) (KNN on MFCC features, needs a dataset that isn't in the repo) and [Python pactise problem](Python%20pactise%20problem/).

## Running things locally

There's no single install for everything. Each folder is its own little script, and most of them were written on Windows.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt   # pygame, pyttsx3, mediapipe, opencv-python, pycaw, comtypes, pyautogui, many other things depending on the project
```

That covers Flappy Bird, Lazy Controller, Gym and Motion detector. For the others, install what the imports ask for, e.g. `requests`, `pandas`, `phonenumbers`, `pytube`, `pillow`, `SpeechRecognition`, `keyboard`, `pywin32`.

Run scripts from inside their folder, since a lot of them use relative paths:

```bash
cd "Flappy Bird"
python flappy_bird.py
```

Heads up: a few scripts still have hardcoded paths from my machine (Investor, Instagram Data Analyser, Text From Speech), so you'll need to change those before running them.

---

This is a messy, ongoing collection. I add things when I get curious about something, and some of it will probably stay half-done 🙂
