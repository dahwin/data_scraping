from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up the options for the Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# URL of the webpage
url = "https://deepmind.google/discover/blog/transforming-the-future-of-music-creation/"

# Open the webpage
driver.get(url)

# Wait for the page to load (you might need to adjust the time based on your internet speed)
driver.implicitly_wait(10)

# Get all text from the page
all_text_elements = driver.find_elements(By.TAG_NAME, "body")

# Iterate through the elements and get text
all_text = [element.text for element in all_text_elements]

# Print or use the text as needed
print(all_text)

# Close the WebDriver
driver.quit()
