from selenium import webdriver
import os
import time
import pyautogui
from playsound import playsound

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,'chromedriver.exe')
soundname = os.path.join(dirname,'giveyouup.mp3')
browser = webdriver.Chrome(filename)
browser.get('https://www.amd.com/en/direct-buy/5458372800/us')
soldout = pyautogui.locateCenterOnScreen("outofstock.png")
flag = 0
lastsold = None

while flag == 0:
    try:
        browser.find_element_by_xpath('//*[@id="product-details-info"]/div[2]/div/div[2]/ul/li[8]/a').click()
        lastsold = soldout
        soldout = pyautogui.locateCenterOnScreen("outofstock.png")
        if soldout == None:
            pyautogui.click(lastsold)
            playsound(soundname)
            flag = 1
    except:
        pyautogui.click(soldout)