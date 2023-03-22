import time

from bs4 import BeautifulSoup
import requests


web = requests.get('https://socialblade.com/youtube/top/100').text
soup = BeautifulSoup(web, 'lxml')
jobs = soup.find('div')
for index, job in enumerate(jobs):
    posted_date = job.find('span', class_="sim-posted").text
    if 'few' in posted_date:
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
        skills = job.find('span', class_="srp-skills").text.replace(' ', '')
        more_info = job.header.h2.a['href']

print(jobs)