import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
questionlist = []
def getquestions(tag,page):
    url = f'https://stackoverflow.com/questions/tagged/{tag}?tab=newest&page={page}&pagesize=15'

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    qustions = soup.find_all('div',{'class':"s-post-summary--content"})


    for item in qustions:
        qlink = []
        baseurl = 'https://stackoverflow.com'

        title = item.find('h3', {'class':"s-post-summary--content-title"}).text.strip()
        des = item.find('div',{'class':"s-post-summary--content-excerpt"}).text.strip()
        concept = item.find('ul',{'class':"ml0 list-ls-none js-post-tag-list-wrapper d-inline"}).text.strip()
        linklist = item.find('a',{'class':"s-link"})['href']
        qlink.append(baseurl+linklist)
        date = item.find('span',{'class':"relativetime"})['title']
        user = item.find('div', {'class': "s-user-card--link d-flex gs4"}).text.strip()
        qustion = {
            'title': title,
            'concept': concept,
            'description': des,
            'link': qlink,
            'date': date,
            'username': user,

        }

        questionlist.append(qustion)

        print(title)
        print(des)
        print(concept)
        print(qlink)
        print(date)
        print(user)

        print()
        print()

extralist = []
def extra(tag, page):
    url = f'https://stackoverflow.com/questions/tagged/{tag}?tab=newest&page={page}&pagesize=15'

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    #summery = soup.find_all('div', { 'class' : "s-post-summary--stats-item s-post-summary--stats-item__emphasized"})
    summery = soup.find_all('div', { 'class' : "s-post-summary--stats js-post-summary-stats"})
    for q in summery:
        number_of_vote = q.find('div', {'class': "s-post-summary--stats-item s-post-summary--stats-item__emphasized"}).text.strip()
        try:
            number_of_answer = q.find(attrs={'title': 'answer'}).text.strip()
        except:
            number_of_answer = None
        # number_of_views = q.find('div',{'class':"s-post-summary--stats-item"}).text.strip()
        quistion = {
            'number of vote': number_of_vote.replace('\n',' '),
            'number of answer': number_of_answer,
            # 'number of views' : number_of_views,

        }

        extralist.append(quistion)



for p in range(1):
    getquestions("python",p)


for p in range(1):
    extra("python", p)


print(questionlist,extralist)
import pandas
df = pandas.DataFrame(questionlist)
ef = pandas.DataFrame(extralist)
df.to_csv('c++.csv')
ef.to_csv('extrac++.csv')