import requests
from bs4 import BeautifulSoup

def get_page_link(url):
    baseurl = 'https://www.thewhiskyexchange.com'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    links = soup.select('li.product-grid__item a')
    return [baseurl+link.attrs['href'] for link in  links]

def product_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    title = soup.select_one('p.product-card__name').text.strip().replace('\n', '')
    price = soup.select_one('p.product-card__price').text.strip().replace('\n', '')


    description = soup.select_one('div.product-main__description').text.strip().replace('\n', '')
    prduct = print([title, price, description])
    return prduct



print(product_data( 'https://www.thewhiskyexchange.com/search?q=whisky'))
