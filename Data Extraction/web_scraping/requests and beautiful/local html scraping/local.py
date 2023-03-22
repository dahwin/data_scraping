from bs4 import *
import requests
web = open('twice.html' , encoding='utf-8')
soup = BeautifulSoup(web, 'lxml')
tag = soup.find('')