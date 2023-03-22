from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import re
import pandas

url = 'https://docs.python.org/3/library/random.html'
UserAgent = Request(url, headers={'User-Agent':'Mozilla/5.0'})
page = urlopen(url)

soup = BeautifulSoup(page,'lxml')
name = soup.body.findAll('dt', class_ = "sig sig-object py")
fucntion_names = re.findall('id="random.\w+',str(name))
fucntion_names = [item[4:] for  item in fucntion_names]

discriptions = soup.body.findAll('dd')

function_usage = []
for item in discriptions:
    item = item.text
    item = item.replace('\n',' ')
    function_usage.append(item)


#print(fucntion_names)
#print(function_usage)

# data = pandas.DataFrame({'function_names':fucntion_names,'function_usage': function_usage})
# data.to_csv('dahyun.csv')
#print(data)


#large specific attribute

example = soup.body.findAll('section',attrs={'id': 'bookkeeping-functions'})

n = example.a.text


print()
#print(function_usage)