import pyautogui
import time
from playsound import playsound
import os


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,'giveyouup.mp3')
playsound(filename)
print(pyautogui.position())