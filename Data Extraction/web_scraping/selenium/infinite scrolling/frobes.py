# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
# Start a webdriver and navigate to the page
driver = webdriver.Chrome()
driver.get("https://www.forbes.com/real-time-billionaires/#2f2deb243d78")
# Find the element using a CSS selector
elem = driver.find_element(By.CLASS_NAME,'ng-scope.ng-table')

# Scroll to the element
driver.execute_script("arguments[0].scrollIntoView();", elem)

