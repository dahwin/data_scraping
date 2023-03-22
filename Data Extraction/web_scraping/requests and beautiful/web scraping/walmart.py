import json
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0"}
url = "https://www.walmart.com/search?q=70+inch+tv&page=2&affinityOverride=default"
html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.text,'lxml')

all = soup.find_all('div',{'class':'h-100.pb1-xl.pr4-xl.pv1.ph1'})
print(all)