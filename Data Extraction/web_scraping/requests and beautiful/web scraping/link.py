import requests
from bs4 import BeautifulSoup

web = requests.get('https://www.youtube.com/c/TWICE/videos').content
soup = BeautifulSoup(web,'html.parser')


for link in soup.find_all('a'):
    if(link!='#'):
        link = 'https://www.youtube.com/c/TWICE/videos' + link.get('href')

        print(link)


#or

for link in soup.find_all('a'):

     print(link.get('href'))

