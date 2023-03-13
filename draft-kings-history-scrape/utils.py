import pandas as pd
from bs4 import BeautifulSoup
import requests
from time import sleep
import datetime
from random import randint
import os

encoding = 'ISO-8859-1'
def soup(url):
    BASE_DIR="page_cache/"
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    url_hash=url.replace("/","").replace(":","").replace("?","").replace(".","")
    try:
        with open(BASE_DIR+url_hash, "r", encoding=encoding,errors='ignore') as file:
            return BeautifulSoup(file.read(), "html.parser")
    except FileNotFoundError:
        print(url)
        sleep(randint(2,7))
        html_data = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}).text
        soup_data = BeautifulSoup(html_data, "html.parser")
        with open(BASE_DIR+url_hash, "w", encoding=encoding,errors='ignore') as file:
            file.write(html_data)
        return soup_data
    except RuntimeError:
        print(RuntimeError)