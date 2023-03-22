from bs4 import BeautifulSoup
from requests_html import HTMLSession
url = 'https://www.beerwulf.com/en-gb/c?q=beers&type=0'
import requests


r = HTMLSession.get(url)

r.html.render(sleep=1)
product = r.html.find('div.row',first=True)
productinfo = []
for item in product.absolute_links:
    ra = HTMLSession.get(item)

    try:
        style = ra.html.find('dd.small-6 medium-9 columns', first=True)[0].text
    except:
        style = None
    try:
        volume = ra.html.find('dd[data-volume]', first=True).text
    except:
        volume = None
    try:
        ABV = ra.html.find('dd.small-6 medium-9 columns', first=True)[1].text
    except:
        ABV = None
    try:
        origin = ra.html.find('dt[data-country]', first=True).text
    except:
        origin = None
    try:
        description = ra.html.find('div.product-description', first=True).text
    except:
        description = None
    products = {
        'style': style,
        'volulme': volume,
        'ABV': ABV,
        'origin': origin,
        'description': description

    }

    productinfo.append(products)