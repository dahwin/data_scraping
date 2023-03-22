
import requests
from bs4 import BeautifulSoup
baseurl = 'https://www.thewhiskyexchange.com'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

productlinks = []
for x in range(1):
    r = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}')
    b = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky?psize=120')

    soup = BeautifulSoup(b.content,'lxml')

    productlist = soup.select('#content > section.js-filter-products > div > ul')
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl+link['href'])

#testlink = 'https://www.thewhiskyexchange.com/p/29388/hibiki-harmony'
for link in productlinks:
    webrequest = requests.get(link, headers=headers)
    mainsoup = BeautifulSoup(webrequest.content, 'lxml')
    try:#content > article > div.product-page__section.product-page__section--main.product-main > header > h1
        name = mainsoup.select_one('#content > article > div.product-page__section.product-page__section--main.product-main > header > h1').text.strip()
    except:
        name = None


    try:
        rating = mainsoup.find('span', class_="review-overview__count").text.strip()
    except:
        rating = None
    try:
        price = mainsoup.find('p', class_="product-action__price").text.strip()
    except:
        price = None
    try:
        tupe = mainsoup.find('ul', class_="product-main__meta").text.strip()
    except:
        tupe = None

    try:
        description = mainsoup.find('div', class_="product-main__description").text.strip()
    except:
        description = None

    print(name)
    print(price)
    print(tupe)
    print(description)


# import pandas
#
# df = pandas.DataFrame(productlinks)
#
# df.to_csv('alllink.csv')

