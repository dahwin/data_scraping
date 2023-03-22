import aiohttp
from bs4 import BeautifulSoup
import asyncio
import csv
# Open the CSV file and read it into a list of rows
with open('40000.csv', 'r') as f:
    reader = csv.reader(f)
    row5 = list(reader)
rows = row5[0:2]
# Print the list of rows to check that it's correct
data = []
async def main(rows):
    async with aiohttp.ClientSession() as session:
        for row in rows:
            # row[0] is the first column in the CSV, which should contain the URL
            url = row[0]
            async with session.get(url,proxy='http://201.184.72.178:999') as response:
                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])

                html = await response.text()
                soup = BeautifulSoup(html,'lxml')
                name = soup.select('#content-left > section > table > tbody > tr:nth-child(1) > td.provider-name.hidden-xs > a')
                for i in range(len(name)):
                    t = {
                        'name': name[i]
                    }
                    data.append(i)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(rows))
print(data)