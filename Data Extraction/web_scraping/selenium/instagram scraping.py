from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy,ProxyType
import os
import wget
import sys
import time
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option("detach", True)

path = 'G:/chromedriver.exe'
driver = webdriver.Chrome(executable_path=path,options=options)
driver.get('https://instagram.com/')
username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR , "input[name='username']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR , "input[name='password']")))
username.clear()
username.send_keys("webdahyun")
password.clear()
password.send_keys("dawin666999")

button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# find the button element
button = driver.find_element(By.CSS_SELECTOR,".x1n2onr6.x6s0dn4.x78zum5 > a")

# click the button
button.click()