from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Chrome(options=options, executable_path=r"G:/chromedriver.exe")



driver.get("https://www.flipkart.com/search?q=watch&sid=r18%2Cf13&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=watch%7CWrist+Watches&requestId=d64659cc-2125-411f-bd7a-2d09b895305b")

# Locate the "Next" button element using its CSS class
dahwin = []


# options.add_argument("--headless")

isNextDisabled = False

while not isNextDisabled:
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div._1xHGtK._373qXS')))

        div = driver.find_elements(By.CSS_SELECTOR,'div._1xHGtK._373qXS')
        for info in div:
            name = info.find_element(By.CSS_SELECTOR,'.IRpwTa').text
            try:
               First_Price = info.find_element(By.CSS_SELECTOR,'._3I9_wc').text.encode('utf-8', 'ignore').decode('utf-8')

            except:
                First_Price = None
            Price = info.find_element(By.CSS_SELECTOR,'._30jeq3').text.encode('utf-8', 'ignore').decode('utf-8')
            try:
               Discount = info.find_element(By.CSS_SELECTOR,'div._3Ay6Sb').text
            except:
                Discount = None

            img_element = driver.find_element(By.XPATH, '//img[@class="_2r_T1I"]')
            img_src = img_element.get_attribute("src")
            a_element = driver.find_element(By.XPATH, '//a[@class="IRpwTa"]')
            link = a_element.get_attribute("href")
            data= {
                'Name': name,
                'First Price':First_Price,
                'Price':Price,
                'Discount':Discount,
                'Product_link':link,
                'Image Link': img_src
            }
            dahwin.append(data)
            print(data)
        # next_b = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'._1LKTO3')))
        next_b = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='_1LKTO3']/span[text()='Next']")))

        driver.find_element(By.XPATH,"//a[@class='_1LKTO3']/span[text()='Next']").click()
        driver.refresh()
    except Exception as e:
        print(e,'Main Error')
        isNextDisabled = True



import pandas
df = pandas.DataFrame(dahwin)

df.to_csv('data/try.csv')

print(len(dahwin))