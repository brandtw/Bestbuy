import pyautogui
import time

flag = 0
time.sleep(5)

while flag == 0:
    soldout = pyautogui.locateCenterOnScreen("soldout.png")
    addtocart = pyautogui.locateCenterOnScreen("addtocart.png")
    if addtocart != None:
        pyautogui.click(addtocart)
        flag = 1
    elif soldout != None:
        pyautogui.press('f5')
        time.sleep(1)

while True:
    addtocart = pyautogui.locateCenterOnScreen("addtocart.png")
    gotocart = pyautogui.locateCenterOnScreen("gotocart.png")
    checkout = pyautogui.locateCenterOnScreen("checkout.png")
    if addtocart != None:
        pyautogui.click(addtocart)
    if gotocart != None:
        pyautogui.click(gotocart)
    if checkout != None:
        pyautogui.moveTo(80,80)
        pyautogui.click(checkout)