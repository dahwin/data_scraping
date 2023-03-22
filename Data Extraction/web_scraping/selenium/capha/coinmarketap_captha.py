from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

data = []
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://coinmarketcap.com/')
# Switch to the iframe containing the button
# Find the button element and click it
button = driver.find_element(By.CSS_SELECTOR,"button[data-btnname='Log In']")
button.click()


username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR , 'input[placeholder="Enter your email address..."]')))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR , 'input[placeholder="Enter your password..."]')))
username.clear()
username.send_keys("ratulhasan110@yahoo.com")
password.clear()
password.send_keys("JtdtuzKG74r34g#49hfydfjskyfky")
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sc-a4a6801b-0.dPXqEb"))).click()
