from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from playsound import playsound 
import os
import time
from threading import Thread
from webdriver_manager.chrome import ChromeDriverManager

# Main Function
class chromescalp():
        
    def start(self,address,username,password):
        
        # Browser Launch Sequence + Full Screen
        self.flag = False
        self.dirname = os.path.dirname(__file__)
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.browser,6000)
        self.RickRoll = os.path.join(self.dirname,'giveyouup.mp3')
        self.browser.get(address)
        buyButton = False

        # Auto Login
        time.sleep(5)
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.browser.find_element_by_xpath('//*[@id="large-footer"]/div[2]/div[1]/div[1]/ul/li[3]').click()
        self.wait.until(EC.presence_of_element_located((By.ID,"fld-e")))
        self.browser.find_element_by_id("fld-e").send_keys(username)
        self.browser.find_element_by_id("fld-p1").send_keys(password)
        self.browser.find_element_by_class_name("c-checkbox-custom-input").click()
        self.browser.find_element_by_xpath("/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[4]/button").click()

        # Item Selection + Cart + Checkout Automation
        while not buyButton:        
            try:
                self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'fulfillment-add-to-cart-button')))
                self.flag = True
                self.browser.find_element_by_class_name("btn-disabled")
                self.browser.refresh()
                time.sleep(1)            
            except:
                playsound(self.RickRoll, block=False)
                while not buyButton:
                    try:
                        self.browser.find_element_by_class_name('dot')
                        self.browser.find_element_by_class_name("shop-cart-icon").click()
                        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"checkout-buttons")))
                        self.browser.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button').click()
                        buyButton = True
                    except:
                        self.browser.find_element_by_class_name("add-to-cart-button").click()
        
        time.sleep(300)

# GPU http Links

#https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402
# Test http Links
#my_function("https://www.bestbuy.com/site/wd-blue-4tb-internal-sata-hard-drive-for-desktops/9026007.p?skuId=9026007")
#my_function("https://www.bestbuy.com/site/apple-10-2-inch-ipad-latest-model-8th-generation-with-wi-fi-32gb-space-gray/5199701.p?skuId=5199701")