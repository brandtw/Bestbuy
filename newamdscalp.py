import os
import time
import pyautogui
from playsound import playsound

dirname = os.path.dirname(__file__)
soundname = os.path.join(dirname,'giveyouup.mp3')
soldout = pyautogui.locateCenterOnScreen("outofstock.png")
flag = 0
lastsold = None
time.sleep(5)

while flag == 0:
    try:
        fullspec = pyautogui.locateCenterOnScreen("fullspecifications.png")
        pyautogui.click(fullspec)
        lastsold = soldout
        soldout = pyautogui.locateCenterOnScreen("outofstock.png")
        if soldout == None:
            pyautogui.click(lastsold)
            playsound(soundname)
            flag = 1
    except:
        pyautogui.click(soldout)