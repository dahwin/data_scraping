import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Science&txtLocation='
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
job = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for time in job:
    title = time.find('h1', class_='jd-job-title').text.strip()
    company = time.find('h2').text.strip()
    des = time.find('div', class_="jd-desc job-description-main").text.strip()

    print(title)
    print(company)
    print(des)



