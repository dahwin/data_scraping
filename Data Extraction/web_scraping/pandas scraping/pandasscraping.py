'''Dahyun+Darwin = Dahwin'''
import pandas as pd
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# for c in range(1,20):
#     linkall = f'https://www.coingecko.com/?page={c}'
#     driver = webdriver.Chrome()
#     driver.get(linkall)
#     elem = driver.find_element(By.TAG_NAME, 'table')
#
#     head = elem.find_element(By.TAG_NAME, 'thead')
#     body = elem.find_element(By.TAG_NAME, 'tbody')
#
#     list_rows = []
#
#     for items in body.find_elements(By.TAG_NAME, 'tr'):
#         list_cells = []
#         for item in items.find_elements(By.TAG_NAME, 'td'):
#             list_cells.append(item.text)
#         list_rows.append(list_cells)
#     driver.close()
#
#     print(list_rows)
#     print(len(list_rows))
#     df = pd.DataFrame(list_rows)
#     df.to_csv('billion.csv')
#
'''Dahyun+Darwin = Dahwin'''
urll = 'https://en.wikipedia.org/wiki/Dahyun'

data = pd.read_html(urll)[2]

print(data)