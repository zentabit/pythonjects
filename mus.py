import pyautogui
from random import randint

width, height = pyautogui.size()

while True:
    pyautogui.moveTo(randint(0,width), randint(0,height), duration=0.25)
