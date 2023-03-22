from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver  = webdriver.Chrome('G:/chromedriver.exe', chrome_options=chrome_options)
driver.get('https://www.tiktok.com/@twice_tiktok_official?lang=en')
time.sleep(1)
previous_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == previous_height:
        break
    previous_height = new_height
