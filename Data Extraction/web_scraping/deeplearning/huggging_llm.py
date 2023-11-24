from selenium import webdriver
from selenium.webdriver.chrome.options import Options
url = 'https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard'

options = Options()

driver = webdriver.Chrome(options=options)

# Open the URL
driver.get(url)

# Wait for the page to load (adjust the time based on your observation)
driver.implicitly_wait(30)

# Find the element using the CSS selector
product = driver.find_element_by_css_selector('#leaderboard-table')

# Print the found element
print(product.text)

# Close the browser
driver.quit()




