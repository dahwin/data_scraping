from selenium import webdriver
from selenium.webdriver.chrome.options import Options
option1 = Options()
option1.add_argument('--disable-notifications')
driver = webdriver.Chrome(executable_path="C:/Program Files/chromedriver.exe",chrome_options=option1)