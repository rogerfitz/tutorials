import random
from config import USERNAME,PASSWORD
import os,sys
from time import sleep
import random
from selenium import webdriver
from decimal import Decimal
from re import sub

def purchaseProduct(MAX_BUY_PRICE, PRODUCT_PAGE):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : os.getcwd()+"/data"}
    chromeOptions.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)  # Optional argument, if not specified will search path.

    driver.get(PRODUCT_PAGE)
    driver.find_element_by_id("nav-link-accountList").click()
    def randomSleep(scale_factor=1):
        sleep_dur=.1*scale_factor*random.randint(1,3)
        print("Sleeping for:", sleep_dur, flush=True)#flush needed to make sure output gets written in timely matter
        sleep(sleep_dur)
    randomSleep()
    driver.find_element_by_id('ap_email').send_keys(USERNAME)
    driver.find_element_by_id('ap_password').send_keys(PASSWORD)
    driver.find_element_by_id("a-autoid-0").click()

    driver.find_element_by_id("add-to-cart-button").click()
    driver.find_elements_by_xpath("//*[@aria-label='Close']")[0].click()
    driver.get("https://www.amazon.com/gp/cart/view.html/ref=lh_co?ie=UTF8&proceedToCheckout.x=129&hasWorkingJavascript=1")
    randomSleep()
    driver.find_elements_by_xpath("//*[@aria-labelledby='orderSummaryPrimaryActionBtn-announce']")[0].click()
    sleep(3)
    driver.find_elements_by_xpath("//*[@aria-labelledby='orderSummaryPrimaryActionBtn-announce']")[0].click()
    priceOk=False
        
    from bs4 import BeautifulSoup as soup

    table=soup(driver.find_element_by_id("subtotalsContainer").get_attribute("innerHTML"),"lxml")

    total=table.find("td","a-color-price a-size-medium a-text-right a-align-bottom aok-nowrap grand-total-price a-text-bold").text
    try:
        total_amount=Decimal(sub(r'[^\d.]', '', total))
        if total_amount<=MAX_BUY_PRICE:
            priceOk=True
        else:
            print(total_amount, 'Price is too high')
    except:
        print("Could not parse", total.text)
        
    if priceOk:
        driver.find_elements_by_xpath("//*[@aria-labelledby='submitOrderButtonId-announce']")[0].click()
        print("purchased")
    driver.quit()

if __name__=="__main__":
    MAX_BUY_PRICE=0
    PRODUCT_PAGE="https://www.amazon.com/Amazon-Echo-Dot-Portable-Bluetooth-Speaker-with-Alexa-Black/dp/B01DFKC2SO/"
    QUANTITY=3
    for i in range(QUANTITY):
        purchaseProduct(MAX_BUY_PRICE, PRODUCT_PAGE)