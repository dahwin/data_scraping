# import pandas as pd

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

list_rows = []
for c in range(1,101):
   linkall = f'https://www.coingecko.com/?page={c}'

   options = Options()
   options.headless = True
   driver = webdriver.Chrome(options=options)

   driver.get(linkall)
   elem = driver.find_element(By.TAG_NAME, 'table')

   head = elem.find_element(By.TAG_NAME, 'thead')
   body = elem.find_element(By.TAG_NAME, 'tbody')

   for items in body.find_elements(By.TAG_NAME, 'tr'):
       list_cells = []
       for item in items.find_elements(By.TAG_NAME, 'td'):
           list_cells.append(item.text)
       list_rows.append(list_cells)
   driver.close()




print(list_rows)
print(len(list_rows))
# df = pd.DataFrame(list_rows)
# df.to_csv('coingeckoall.csv')



