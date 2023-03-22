from selenium import webdriver
import time

# create a new Chrome browser and navigate to YouTube
driver = webdriver.Chrome()
driver.get('https://play.google.com/store/search?q=social%20media&c=apps&hl=en&gl=US')

# wait for the page to fully load
driver.implicitly_wait(10)

# get the current height of the page
previous_height = driver.execute_script('return document.body.scrollHeight')

# create a loop to scroll down the page indefinitely
while True:
    # scroll down to the bottom of the page
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    # wait for the page to load the new content
    time.sleep(2)

    # get the new height of the page
    new_height = driver.execute_script('return document.body.scrollHeight')

    # check if the page height has changed
    if new_height == previous_height:
        # if the page height has not changed, the page has reached the end
        # and we can break out of the loop
        break

    # update the previous height for the next iteration
    previous_height = new_height
