"""Python POC to move mouse cursor after every 2.5 minutes in order to stop system from locking"""

import datetime
import pyautogui
from time import sleep
import random

while True:
    print(datetime.datetime.now())
    initial_position = pyautogui.position()
    print(f"Initial Position: {str(initial_position)}")
    sleep(150)
    print(f"Position after 2.5 minutes{pyautogui.position()}")
    if initial_position == pyautogui.position():
        pyautogui.moveTo(random.randint(0, 1080), random.randint(0, 1080), duration=1)
        pyautogui.moveTo(random.randint(0, 1080), random.randint(0, 1080), duration=1)
        pyautogui.moveTo(random.randint(0, 1080), random.randint(0, 1080), duration=1)
        pyautogui.scroll(clicks=1)
        pyautogui.moveTo(random.randint(0, 1080), random.randint(0, 1080), duration=1)
        pyautogui.moveTo(random.randint(0, 1080), random.randint(0, 1080), duration=1)
        pyautogui.moveTo(random.randint(0, 1080), random.randint(0, 1080), duration=1)
        print("Moved Mouse and Clicked!!!")
    else:
        print(f"New Position: {str(pyautogui.position())}")


