from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# create a new Chrome browser and navigate to YouTube
driver = webdriver.Chrome()
driver.get('https://www.nike.com/w/new-3n82y')

# wait for the page to fully load
driver.implicitly_wait(10)

# get the current height of the page
previous_height = driver.execute_script('return document.body.scrollHeight')

# create a loop to scroll down the page indefinitely
while True:
    # scroll down to the bottom of the page
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    # wait for the page to load the new content
    time.sleep(6)

    # get the new height of the page
    new_height = driver.execute_script('return document.body.scrollHeight')

    # check if the page height has changed
    if new_height == previous_height:
        # if the page height has not changed, the page has reached the end
        # and we can break out of the loop
        break

    # update the previous height for the next iteration
    previous_height = new_height
# once the page has fully loaded, we can start scraping the data we want
# for example, let's scrape the names and prices of the products on the page
products = driver.find_elements(By.CSS_SELECTOR,'grid-item .product-card .product-card__body .product-card__title')
prices = driver.find_elements(By.CSS_SELECTOR,'.grid-item .product-card .product-card__body .product-card__price')

# loop through the products and prices and print them
for product, price in zip(products, prices):
    print(product.text + ': ' + price.text)

# don't forget to close the browser when you're done
driver.close()
