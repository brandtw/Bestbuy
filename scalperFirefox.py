from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from playsound import playsound 
import os
import time
from threading import Thread

# Username and Password User Input
print("\n!!!!!!!!!!!!!!!!! MAKE SURE YOUR INFORMATION IS 100% CORRECT. DOUBLE CHECK. !!!!!!!!!!!!!!!!!")
username = input("Username: ")
password = input("Password: ")                                                                 

# Main Function
def my_function(address):

    # Main Prototyping  
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname,'geckodriver.exe')
    browser = webdriver.Firefox(executable_path = filename)
    RickRoll = os.path.join(dirname,'giveyouup.mp3')
    wait = WebDriverWait(browser,6000)                      # Webpage timeout set to max 6000 seconds  
    
    # Browser Launch Sequence + Full Screen
    browser.get(address)
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
            wait.until(EC.presence_of_element_located((By.CLASS_NAME,'fulfillment-add-to-cart-button')))
            browser.find_element_by_class_name("btn-disabled")
            browser.refresh()            
        except:
            playsound(RickRoll, block=False)
            while not buyButton:
                try:
                    browser.find_element_by_xpath('//*[@id="shop-cart-icon-02c028e8-4638-43e6-96ff-96d1c70cfe72"]/div/div/div/a/div')
                    browser.find_element_by_class_name("shop-cart-icon").click()
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"checkout-buttons")))
                    browser.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button').click()
                    buyButton = True
                except:
                    browser.find_element_by_class_name("add-to-cart-button").click()
    
    time.sleep(300)


# GPU http Links

thread1 = Thread(target = my_function, args=("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402",))
#thread2 = Thread(target = my_function, args=("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442",))
#thread3 = Thread(target = my_function, args=("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440",))
#thread4 = Thread(target = my_function, args=("https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434",))
thread1.start()
# time.sleep(5)
# thread2.start()
# time.sleep(5)
# thread3.start()
# time.sleep(5)
# thread4.start()

#thread5 = Thread(target = my_function, args=("https://www.bestbuy.com/site/wd-blue-4tb-internal-sata-hard-drive-for-desktops/9026007.p?skuId=9026007",))
#thread5.start()




# Test http Links
#my_function("https://www.bestbuy.com/site/wd-blue-4tb-internal-sata-hard-drive-for-desktops/9026007.p?skuId=9026007")
#my_function("https://www.bestbuy.com/site/apple-10-2-inch-ipad-latest-model-8th-generation-with-wi-fi-32gb-space-gray/5199701.p?skuId=5199701")