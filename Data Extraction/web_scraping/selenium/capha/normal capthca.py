from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

data = []
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://2captcha.com/demo/normal')
captcah_img = driver.find_element(By.CLASS_NAME,'_17bwEOs9gv8ZKqqYcEnMuQ')
captcah_img.screenshot('captcha_img/captcha.png')

import os

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'dfe042fc7e863e9674e903460b3eeaca')

solver = TwoCaptcha(api_key)

try:
    result = solver.normal('captcha_img/captcha.png')

except Exception as e:
    print(e)

else:
    code = result['code']
    print(code)
    WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID,'simple-captcha-field'))
    driver.find_element(By.ID,'simple-captcha-field').send_keys(code)
    driver.find_element(By.CLASS_NAME,'_2iYm2u0v9LWjjsuiyfKsv4 _1z3RdCK9ek3YQYwshGZNjf _3zBeuZ3zVV-s2YdppESngy _28oc7jlCOdc1KAtktSUZvQ').click()