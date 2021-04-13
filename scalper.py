# To do: threading, consider IF function for survey, fix comments below, during threading maybe have multiple accounts?

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from playsound import playsound 
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
RickRoll = os.path.join(dirname,'giveyouup.mp3')
wait = WebDriverWait(browser,6000)                      # Webpage timeout set to max 6000 seconds                                                                     

# Main Function
def my_function(address):
    
    # Browser Launch Sequence + Full Screen
    browser.get(address)
    browser.maximize_window()
    buyButton = False

    # Auto Login
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
            wait.until(EC.presence_of_element_located((By.CLASS_NAME,'fulfillment-add-to-cart-button')))        # BRANDT, I had to change this. Talk to me before editing.
            browser.find_element_by_class_name("btn-disabled")
            browser.refresh()            
        except:
            while not buyButton:
                try:
                    browser.find_element_by_class_name("add-to-cart-button").click()                        # ADD TO CART BUTTON CLICK
                    #playsound(RickRoll, block=False)
                    EC.presence_of_element_located((By.CLASS_NAME, "added-to-cart-button"))
                    #wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="shop-cart-icon-02c028e8-4638-43e6-96ff-96d1c70cfe72"]/div/div/div/a/div'))) 
                    browser.find_element_by_class_name("shop-cart-icon").click()
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"checkout-buttons")))
                    browser.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button').click() # Chase: Consider changing
                    buyButton = True
                except:
                    pass


# # Threading Objects
# t1 = threading.Thread(target=my_function1)
# t2 = threading.Thread(target=my_function2)
# # g3 = gpu3080()
# # g4 = gpu3090()

# t1.start()
# t2.start()
# # g3.start()
# # g4.start()

# t1.join()
# t2.join()

# GPU http Links
# my_function("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402")         # 3060 ti
# my_function("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442")    # 3070
# my_function("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")       # 3080
#my_function("https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434")       # 3090

# Test http Links
#my_function("https://www.bestbuy.com/site/wd-blue-4tb-internal-sata-hard-drive-for-desktops/9026007.p?skuId=9026007")
my_function("https://www.bestbuy.com/site/apple-10-2-inch-ipad-latest-model-8th-generation-with-wi-fi-32gb-space-gray/5199701.p?skuId=5199701")


# Survey Invite button ID = survey_invite_no <--------------- INSERT IF FUNCTION TO CLICK NO HERE?
# Survey Invite border ID = survey_border