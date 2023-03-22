from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
data = []
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
dahwin = []
driver.get('https://www.zillow.com/')
singin = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR , "ul[data-zg-section='reg-login'] a.Anchor-c11n-8-62-4__sc-hn4bge-0")))
# all = driver.find_element(By.CSS_SELECTOR,'ul.List-c11n-8-73-8__sc-1smrmqp-0.srp__sc-1psn8tk-0.bfcHMx.photo-cards.with_constellation')
# div = all.find_elements(By.CSS_SELECTOR,'li.ListItem-c11n-8-73-8__sc-10e22w8-0.srp__hpnp3q-0.enEXBq.with_constellation')
# time.sleep(10)
# for info in div:
#     try:
#       address = info.find_element(By.CSS_SELECTOR,"address[data-test='property-card-addr']").text
#     except:
#         address=None
#     try:
#        First_Offer = info.find_element(By.CSS_SELECTOR,'div.StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0.hRqIYX').text
#     except:
#         First_Offer=None
#     try:
#        Second_Offer = info.find_element(By.CSS_SELECTOR,"div.StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0.ghGYOB").text
#     except:
#         Second_Offer=None
#     # Third_Offer = info.find_element(By.CSS_SELECTOR,'')
#
#     data = {
#         'Address':address,
#         'First_Offer':First_Offer,
#         'Second_Offer':Second_Offer
#     }
#     dahwin.append(data)
#
# print(dahwin)

