'''dahyun+darwin = dahwin'''
# import asyncio
# import aiohttp
# import pandas as pd
# from bs4 import BeautifulSoup
#
# async def scrape_link(session, link):
#     async with session.get(link) as response:
#         data = await response.text()
#         soup = BeautifulSoup(data, 'html.parser')
#         # Parse the data using BeautifulSoup here and return the result
#         result = soup.select_one('a',class_='mx-3').text.strip()
#         return result
#
# async def scrape_links(links):
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for link in links:
#             task = asyncio.ensure_future(scrape_link(session, link))
#             tasks.append(task)
#         results = await asyncio.gather(*tasks)
#         # Save the results to a CSV file
#         # df = pd.DataFrame(results, columns=['column1', 'column2', ...])
#         # df.to_csv('output.csv', index=False)
#         print(results)
#
# # Load the links from a CSV file
# df = pd.read_csv("G:\\download\\vacasa.csv")
# links = df['Link'][3:]
#
# # Scrape the links asynchronously
# loop = asyncio.get_event_loop()
# loop.run_until_complete(scrape_links(links))

import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
df = pd.read_csv("G:\\download\\vacasa.csv")
links = df['Link']
data = []
for link in links:
    webrequest = requests.get(link, headers=headers)
    mainsoup = BeautifulSoup(webrequest.content, 'lxml')
    try:
        review = mainsoup.select_one(
            'body > div.container.type-body-small.mt-5.unit-container > div:nth-child(4) > a').text.strip()
    except:
        review= '0'
    rview = re.findall('\d+', review)[0]
    d = {
        'Review':rview
    }
    data.append(d)
print(data)
import pandas
df = pd.DataFrame(data)
df.to_csv('dahwindata.csv')


