from selenium import webdriver
import time
import threading

browser = webdriver.Chrome("C:/Users/brand/OneDrive/Documents/Coding/Bestbuy/chromedriver.exe")

def my_function(address):
    browser.get(address)
    buyButton = False

    while not buyButton:
            try:
                #addtocartbtn = browser.find_element_by_class_name("btn-disabled")
                addtocartbtn = browser.find_element_by_xpath("//button[contains(@class, 'btn-disabled')]")
                time.sleep(1)
                browser.refresh()
            except:
                try:
                    browser.find_element_by_class_name("add-to-cart-button").click()
                    time.sleep(1)
                    browser.find_element_by_xpath("/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a").click()
                    time.sleep(1)
                    #browser.find_element_by_xpath("/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button").click()
                    browser.find_element_by_class_name("btn-primary").click()

                except:
                    buyButton = True

#my_function("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
my_function("https://www.bestbuy.com/site/wd-blue-4tb-internal-sata-hard-drive-for-desktops/9026007.p?skuId=9026007")