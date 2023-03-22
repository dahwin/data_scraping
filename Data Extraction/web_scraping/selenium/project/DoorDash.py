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
driver.get('https://identity.doordash.com/auth?client_id=1666519390426295040&layout=consumer_web&prompt=none&redirect_uri=https%3A%2F%2Fwww.doordash.com%2F&response_type=code&scope=%2A&state=none')

