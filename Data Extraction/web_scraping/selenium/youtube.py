from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver  = webdriver.Chrome('G:/chromedriver.exe', chrome_options=chrome_options)
driver.get('https://www.youtube.com/@TWICE/videos')
vdata = []

def brower():

    data = driver.find_elements(By.XPATH, '//*[@id="contents"]')

    for dahyun in data:
        title = dahyun.find_element(By.CSS_SELECTOR,'ytd-rich-grid-media[mini-mode] #video-title.ytd-rich-grid-media').text

        view = dahyun.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(3)').text
        date = dahyun.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(4)').text
        d = {
            'title': title,
            'view': view,
            'date': date
        }
        vdata.append(d)
    print(vdata)
    print(len(vdata))
brower()
#
#
#
