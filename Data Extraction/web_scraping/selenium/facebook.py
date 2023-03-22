#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
#code by pythonjar, not me
chrome_options = webdriver.ChromeOptions()
#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome( chrome_options=chrome_options)

#open the webpage
driver.get("http://www.facebook.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys("bayezidloverumi@gmail.com")
password.clear()
password.send_keys("JtdtuzKG74r34g#49hfydfjskyfky")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!
# wait 5 seconds to allow your new page to load
time.sleep(5)
images = []

# itterate over both uploaded and tagged images respectively
for i in ["photos_all", "photos_of"]:
    # ************************************************
    # !! change goldie.may.750 to your own address !!
    # ************************************************
    driver.get("https://www.facebook.com/goldie.may.750/" + i + "/")
    time.sleep(5)

    # scroll down
    # increase the range to sroll more
    # example: range(0,10) scrolls down 650+ images
    for j in range(0, 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)

    # target all the link elements on the page
    anchors = driver.find_elements(By.TAG_NAME,'a')
    anchors = [a.get_attribute('href') for a in anchors]
    # narrow down all links to image links only
    anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]

    print('Found ' + str(len(anchors)) + ' links to images')

    # extract the [1]st image element in each link
    for a in anchors:
        driver.get(a)  # navigate to link
        time.sleep(5)  # wait a bit
        img = driver.find_elements(By.TAG_NAME,"img")
        images.append(img[1].get_attribute("src"))  # may change in future to img[?]

print('I scraped ' + str(len(images)) + ' images!')
import os

path = os.getcwd()
path = os.path.join(path, "FB_SCRAPED")

#create the directory
os.mkdir(path)
import wget

#download images
counter = 0
for image in images:
    save_as = os.path.join(path, str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1