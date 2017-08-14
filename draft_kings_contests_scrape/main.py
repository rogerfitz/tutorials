import os
from time import sleep
import datetime
import random
from selenium import webdriver
from config import DK_PASSWORD, DK_USERNAME
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : os.getcwd()+"/data"}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)  # Optional argument, if not specified will search path.

def randomSleep(scale_factor=1):
	sleep_dur=.5*scale_factor*random.randint(5,10)*random.randint(1,3)
	print("Sleeping for:", sleep_dur, flush=True)#flush needed to make sure output gets written in timely matter
	sleep(sleep_dur)

driver.get("http://www.draftkings.com")
randomSleep()
sign_in = driver.find_element_by_link_text('SIGN IN')
sign_in.click()
randomSleep(.5)
driver.find_element_by_name('username').send_keys(DK_USERNAME)
randomSleep(.001)
driver.find_element_by_name('username').send_keys("\t"+DK_PASSWORD)
randomSleep(.01)
driver.find_elements_by_xpath("//*[contains(text(), 'LOG IN')]")[0].click()
randomSleep(.1)
#driver.get("https://www.draftkings.com/lobby#/NFL")
driver.find_element_by_link_text("NFL").click()
randomSleep(.1)
driver.find_elements_by_xpath("//*[contains(text(), 'View Live Contests')]")[0].click()
randomSleep(.5)
prize_pool=driver.find_elements_by_css_selector("div.ui-state-default.slick-header-column.grid-text-with-icon")[2]
prize_pool.click()
prize_pool.click()


from bs4 import BeautifulSoup as soup
import pandas as pd
table=soup(driver.find_element_by_id("lobby-grid").get_attribute("innerHTML"),"lxml")
rows=[]
for row in table.find("div","grid-canvas").find_all("div","slick-row"):
    row_data={}
    for cell in row.find_all("div"):
        if cell.find("a"):
            a=cell.find("a")
            if a.get("data-tracking"):
                row_data[a.get("data-tracking")]=cell.text
            if cell.text=="Watch":
                row_data['link']=a.get("href")
    rows.append(row_data)
live_contests=pd.DataFrame(rows)#missing some elements that you need to scroll for

def get_lineups(link):
    randomSleep(4)
    BASE_URL="https://www.draftkings.com"
    driver.get(BASE_URL+link)
    driver.find_element_by_id("export-lineups-csv").click()

live_contests['time_pulled']=datetime.datetime.now().strftime("%Y-%m-%d %I")
contests['link'].apply(get_lineups)
file_name="NFL_contests.csv"
try:
	old_contests=pd.read_csv(file_name)
	full_contests=pd.concat([old_contests,live_contests]).drop_duplicates(subset=["link"])
except:
	print("No file %s found. Creating new."%file_name)
	full_contests=live_contests

full_contests.to_csv(file_name)

#run every sunday at 8PM CST