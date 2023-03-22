import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.thewhiskyexchange.com'
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
#
# productlinks = []
# for x in range(1):
#     r = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}')
#     b = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky?psize=120')
#
#     soup = BeautifulSoup(b.content,'lxml')
#
#     productlist = soup.select('#content > section.js-filter-products > div > ul')
#     for item in productlist:
#         for link in item.find_all('a', href=True):
#             productlinks.append(baseurl+link['href'])

#testlink = 'https://www.thewhiskyexchange.com/p/29388/hibiki-harmony'
df = pd.read_csv("C:\\Users\\Pc\\Desktop\\python\\pandas\\dahyunlovedarwin.csv")
links = df['LINK']
for link in links:
    webrequest = requests.get(link, headers=headers)
    mainsoup = BeautifulSoup(webrequest.content, 'lxml')
    name = mainsoup.select_one('#site-content > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div > div > div > div > section > div._1qdp1ym > div._dm2bj1 > span:nth-child(3) > button > span').text.strip()


    print(name)
