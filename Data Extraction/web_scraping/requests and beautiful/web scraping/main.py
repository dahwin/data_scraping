import time

from bs4 import BeautifulSoup
import requests

print('put some skill that you are not familiar with')
unfamiliar_skill = input(':')
print(f'filtering out {unfamiliar_skill}')

def find_jobs():
    web = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchName=recentSearches&from=submit&actualTxtKeywords=Data%20Scientist&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=data%20scientist&gadLink=data%20scientist').text
    soup = BeautifulSoup(web,'lxml')
    jobs = soup.find_all('li',class_ ="clearfix job-bx wht-shd-bx" )
    for index,job in enumerate(jobs):
        posted_date = job.find('span', class_ = "sim-posted").text
        if 'few' in posted_date:
            company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','')
            skills = job.find('span', class_ = "srp-skills").text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'{index}.xlsx','w') as wf:

                    wf.write(f"Company Name : {company_name.strip()} ")
                    wf.write(f'Skills : {skills.strip()}')
                    wf.write(f'Job posted: {posted_date.strip()}')
                    wf.write(f'More Information:{more_info}')

                    wf.write('')





if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting{time_wait}')
        time.sleep(time_wait*60)