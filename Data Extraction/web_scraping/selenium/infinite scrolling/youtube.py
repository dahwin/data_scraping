# from selenium import webdriver
# import time
#
# # create a new Firefox browser and navigate to YouTube
# driver = webdriver.Firefox(executable_path='"G:\geckodriver.exe"')
# driver.get('https://www.youtube.com/@TWICE/videos')
#
# # wait for the page to fully load
# driver.implicitly_wait(10)
#
# # get the current height of the page
# previous_height = driver.execute_script('return document.body.scrollHeight')
#
# # create a loop to scroll down the page indefinitely
# while True:
#     # scroll down to the bottom of the page
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#
#     # wait for the page to load the new content
#     time.sleep(2)
#
#     # get the new height of the page
#     new_height = driver.execute_script('return document.body.scrollHeight')
#
#     # check if the page height has changed
#     if new_height == previous_height:
#         # if the page height has not changed, the page has reached the end
#         # and we can break out of the loop
#         break
#
#     # update the previous height for the next iteration
#     previous_height = new_height
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com/@TWICE/videos")

while True:
    scroll_height = 2000
    document_height_before = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script(f"window.scrollTo(0, {document_height_before + scroll_height});")
    time.sleep(1.5)
    document_height_after = driver.execute_script("return document.documentElement.scrollHeight")
    if document_height_after == document_height_before:
        break