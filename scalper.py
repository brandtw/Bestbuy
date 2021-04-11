# To do: beeper, threading, continuously click "please wait" IF it appears, fix comments below, during threading maybe have multiple accounts?

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from playsound import playsound
import pyautogui
import os
import time
import threading

# Username and Password User Input
print("\n!!!!!!!!!!!!!!!!! MAKE SURE YOUR INFORMATION IS 100% CORRECT. DOUBLE CHECK. !!!!!!!!!!!!!!!!!")
username = input("Username: ")
password = input("Password: ")

# Main Prototyping
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,'chromedriver.exe')
browser = webdriver.Chrome(filename)
soundname = os.path.join(dirname,'giveyouup.mp3')       # We should thread this sound when the bot clicks "Add to Cart" to notify the user that the item is now in stock.
wait = WebDriverWait(browser,40)                        # Webpage timeout set to max 40 seconds                                                                     

# Main Function
def my_function(address):
    
    # Browser Launch Sequence + Full Screen
    browser.get(address)
    pyautogui.hotkey('winleft', 'up')
    buyButton = False

    # Auto Login (FIXED)
    time.sleep(3)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    browser.find_element_by_xpath('//*[@id="large-footer"]/div[2]/div[1]/div[1]/ul/li[3]').click()
    wait.until(EC.presence_of_element_located((By.ID,"fld-e")))
    browser.find_element_by_id("fld-e").send_keys(username)
    browser.find_element_by_id("fld-p1").send_keys(password)
    browser.find_element_by_class_name("c-checkbox-custom-input").click()
    browser.find_element_by_xpath("/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[4]/button").click()

    # Item Selection + Cart + Checkout Automation
    while not buyButton:        
        try:                 
            outofstockbtn = browser.find_element_by_xpath("//button[contains(@class, 'btn-disabled')]") #._execute(Command.IS_ELEMENT_ENABLED)[False] # This works, but there is a bug when you sign in first. Then it won't refresh the page for some reason. I even tried pyautogui.hotkey('f5')
            browser.refresh()
        except:
            try:                                                        
                wait.until(EC.presence_of_element_located((By.CLASS_NAME,"add-to-cart-button")))        # Sleep until button is clickable
                browser.find_element_by_class_name("add-to-cart-button").click()                        # ADD TO CART BUTTON CLICK. We should thread in a sound here to notify user.
                wait.until(EC.presence_of_element_located((By.CLASS_NAME,"spinner-sm"))) == None        # Checks to see if 'add to cart' action is still loading. Does this work?
                #Here is where we might be able to have the computer wait for the "please wait" to convert into a clickable button. Speak with twins.
                browser.find_element_by_class_name("shop-cart-icon").click()                            # Consider adding: if NOT located at 'https://www.bestbuy.com/cart', click shop cart icon again and wait. Else, click checkout button...
                browser.find_element_by_class_name("btn-primary").click()                               
            except:
                buyButton = True


# Threading Objects
# t1 = threading.Thread(target=gpu3060ti)
# t2 = gpu3070()
# g3 = gpu3080()
# g4 = gpu3090()

# t1.start()
# g2.start()
# g3.start()
# g4.start()

# t1.join()


# GPU http Links
#my_function("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402")         # 3060 ti
# my_function("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442")    # 3070
# my_function("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")       # 3080
#my_function("https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434")       # 3090

# Test http Links
#my_function("https://www.bestbuy.com/site/wd-blue-4tb-internal-sata-hard-drive-for-desktops/9026007.p?skuId=9026007")
my_function("https://www.bestbuy.com/site/apple-10-2-inch-ipad-latest-model-8th-generation-with-wi-fi-32gb-space-gray/5199701.p?skuId=5199701")


# Survey Invite button ID = survey_invite_no <--------------- INSERT IF FUNCTION TO CLICK NO HERE?
# Survey Invite border ID = survey_border