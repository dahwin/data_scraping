# from selenium import webdriver
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver import ActionChains
# data = []
# profile_path = 'C:\\Users\\Shofiullah\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
#
#
# for r in range(1,25):
#     link = f'https://www.walmart.com/search?q=70+inch+tv&page={r}&affinityOverride=default'
#     options = webdriver.ChromeOptions()
#     # options.add_argument("--headless")
#     options.add_argument(f'user-data-dir={profile_path}')
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=options)
#     driver.get(link)
#     button = driver.find_element(By.CSS_SELECTOR,'div#tEDMskgdLdfCdkW')
#     actions = ActionChains(driver)
#     actions.click_and_hold(button)
#     actions.perform()
#     time.sleep(25)
#     actions.release()
#     actions.perform()
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
# Set the path to the Chrome executable
chrome_exe_path = r'G:/chromedriver.exe'

# Create a ChromeService object
service = ChromeService(executable_path=chrome_exe_path)
service.start()
# Create a ChromeOptions object and configure it with the desired options
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\\Users\\Shofiullah\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument(r'--profile-directory=C:\\Users\\Shofiullah\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
options.add_experimental_option("detach", True)

# Create a Chrome webdriver using the service and options
driver = webdriver.Chrome(service=service, options=options)

# Use the webdriver to open a website
driver.get('https://www.walmart.com/search?q=70+inch+tv&page=2&affinityOverride=default')
