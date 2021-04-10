# To do: beeper, threading, continuously click "please wait" IF it appears, quickest possible way to get to the checkout button
# Add logic so the user has to input the password twice and the program checks to see if the passwords match.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui
import os
import time
import threading

# Username and Password input
print(" ")
print("!!!!!!!!!!!!!!!!! MAKE SURE YOUR INFORMATION IS 100% CORRECT. DOUBLE CHECK. !!!!!!!!!!!!!!!!!")
username = input("Username: ")
password = input("Password: ")

# Browser Launch
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,'chromedriver.exe')
browser = webdriver.Chrome(filename)

# Main Function
def my_function(address):
    browser.get(address)
    buyButton = False

    while not buyButton:
            try:
                # addtocartbtn = browser.find_element_by_class_name("btn-disabled")
                addtocartbtn = browser.find_element_by_xpath("//button[contains(@class, 'btn-disabled')]")  # Research way to keep code from waiting for website to load?
                time.sleep(1)
                browser.refresh()
            except:
                try:
                    wait=WebDriverWait(browser,15)                                                          # Timeout max 15 seconds
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"add-to-cart-button")))        # Sleep until button is clickable -- Here is where we might be able to have the computer wait for the "please wait" to convert into a clickable button. Speak with twins
                    browser.find_element_by_class_name("add-to-cart-button").click()                        # ADD TO CART BUTTON CLICK
                    browser.find_element_by_class_name("shop-cart-icon").click()                            # if NOT located at 'https://www.bestbuy.com/cart', click shop cart icon again and wait. Else, click checkout button...
                    browser.find_element_by_class_name("btn-primary").click()                               # CHECKOUT BUTTON CLICK

                    # Auto-Login
                    wait.until(EC.presence_of_element_located((By.ID,"fld-p1")))
                    username_field = browser.find_element_by_id("fld-e")
                    username_field.send_keys(username)
                    password_field = browser.find_element_by_id("fld-p1")
                    password_field.send_keys(password)
                    browser.find_element_by_xpath("/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[3]/button").click()

                except:
                    buyButton = True


# GPU http Links:
#my_function("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
#my_function("https://www.bestbuy.com/site/wd-blue-4tb-internal-sata-hard-drive-for-desktops/9026007.p?skuId=9026007")
my_function("https://www.bestbuy.com/site/apple-10-2-inch-ipad-latest-model-8th-generation-with-wi-fi-32gb-space-gray/5199701.p?skuId=5199701")