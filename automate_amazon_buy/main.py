import random
from config import USERNAME,PASSWORD
import os,sys
from time import sleep
import random
from selenium import webdriver
from decimal import Decimal
from re import sub

MAX_BUY_PRICE=0
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : os.getcwd()+"/data"}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)  # Optional argument, if not specified will search path.

driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fdp%2FB00X4WHP5E%2Fref%3Dfs_ods_fs_ha_dr%3F_encoding%3DUTF8%26ref_%3Dnav_ya_signin")

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
