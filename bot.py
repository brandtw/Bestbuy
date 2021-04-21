import pyautogui
import time
import os
from playsound import playsound

dirname = os.path.dirname(__file__)
alert = os.path.join(dirname,'morning.mp3')
flag = 0

while flag == 0:
    flag2 = 0
    soldout = pyautogui.locateCenterOnScreen("soldout.png", confidence= 0.9)
    addtocart = pyautogui.locateCenterOnScreen("addtocart.png", confidence= 0.7)
    if addtocart != None:
        playsound(alert, block=False)
        pyautogui.click(addtocart)
        time.sleep(1)
        flag = 1
    elif soldout != None:
        pyautogui.press('f5')
        time.sleep(3)

while True:
    addtocart = pyautogui.locateCenterOnScreen("addtocart.png", confidence= 0.7)
    gotocart = pyautogui.locateCenterOnScreen("gotocart.png", confidence= 0.7)
    checkout = pyautogui.locateCenterOnScreen("checkout.png", confidence= 0.9)
    if addtocart != None:
        time.sleep(1)
        pyautogui.click(addtocart)
    if gotocart != None:
        pyautogui.click(gotocart)
    if checkout != None:
        pyautogui.moveTo(80,80)
        pyautogui.click(checkout)