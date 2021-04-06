from selenium import webdriver
import time

browser = webdriver.Chrome("C:/Users/brand/OneDrive/Documents/Coding/Bestbuy/chromedriver.exe")

browser.get("https://www.bestbuy.com/site/apple-watch-series-6-gps-44mm-space-gray-aluminum-case-with-black-sport-band-space-gray/6215931.p?skuId=6215931")

buyButton = False

while not buyButton:
        try:
            addtocartbtn = browser.find_element_by_class_name("btn-disabled")
            time.sleep(1)
            browser.refresh()
        except:
            try:
                browser.find_element_by_xpath("//button[contains(text(), 'Add to Cart')]").click()
            except:
                buyButton = True