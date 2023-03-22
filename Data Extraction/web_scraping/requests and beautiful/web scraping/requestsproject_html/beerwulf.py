from requests_html import HTMLSession
url = 'https://www.beerwulf.com/en-gb/c?q=beers&type=0'
import re

s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1,timeout=20)
product = r.html.xpath('//*[@id="product-items-container"]',first = True)

productinfo = []
for item in product.absolute_links:
    ra = s.get(item)
    name = ra.html.find('h1',first=True).text
    try:
        price = ra.html.find('span.price', first=True).text
    except:
        price = None

    try:
        style = ra.html.find('.medium-9 a',first=True).text
    except:
        style = None
    try:
        volume = ra.html.find('.js-beer-volume',first=True).text
    except:
        volume = None
    try:
        ABV = ra.html.find('.columns:nth-child(6)',first=True).text
    except:
        ABV = None
    try:
        origin = ra.html.find('.js-beer-country', first=True).text
    except:
        origin = None
    try:
        description = ra.html.find('div.product-description', first=True).text
    except:
        description = None
    products = {
        'name' :name,
        'price': price,
        'style': style,
        'volulme':volume,
        'ABV' : ABV,
        'origin' : origin,
        'description':description

    }

    productinfo.append(products)
    print(products)

print(productinfo)
print(len(productinfo))
# import pandas
# df = pandas.DataFrame(productinfo)
# df.to_csv('lastgg.csv')
print(product)