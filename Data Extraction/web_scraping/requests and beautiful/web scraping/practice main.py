import time

from bs4 import BeautifulSoup
import requests




web = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchName=recentSearches&from=submit&actualTxtKeywords=Data%20Scientist&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=data%20scientist&gadLink=data%20scientist').text
soup = BeautifulSoup(web,'lxml')
jobs = soup.find_all('li',class_ ="clearfix job-bx wht-shd-bx" )
for index,job in enumerate(jobs):
        posted_date = job.find('span', class_ = "sim-posted").text
        if 'few' in posted_date:
            company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','')
            skills = job.find('span', class_ = "srp-skills").text.replace(' ', '')
            more_info = job.header.h2.a['href']


            print(f"Company Name : {company_name.strip()} ")
            print(f'Skills : {skills.strip()}')
            print(f'Job posted: {posted_date.strip()}')
            print(f'More Information:{more_info}')

            print('')

