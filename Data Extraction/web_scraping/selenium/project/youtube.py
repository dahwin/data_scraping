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
driver.get('https://www.youtube.com/results?search_query=dahyun')
# # find the search bar element and enter a search query
# search_bar = driver.find_element(By.NAME,'search_query')
# search_bar.send_keys('dahyun')
# search_bar.send_keys(Keys.RETURN)
#
# # wait for the search results to load
# driver.implicitly_wait(10)

# find the search results element
results_element = driver.find_element(By.ID,'contents')

# create a counter to track the number of scrolls
count = 0

# create a loop that will continuously scroll down the page
while True:
    # scroll down the page
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", results_element)

    # increment the counter
    count += 1

    # print the current count
    print(f'Scroll count: {count}')

    # add a delay to allow the page to load
    time.sleep(2)