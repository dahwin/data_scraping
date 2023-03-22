import asyncio
import csv

import aiohttp
csvfile = 'http.csv'
url_to_check = 'https://xvideos.com/'
timeoutinsecond = 10
async def chake_proxy(url,proxy):
    try:
        session_timeout = aiohttp.ClientTimeout(
            total=None,
            sock_connect=timeoutinsecond,
            sock_read=timeoutinsecond,
        )
        async with aiohttp.ClientSession(timeout=session_timeout) as session:
            async  with session.get(
                url, proxy=proxy,timeout=timeoutinsecond
            ) as resp:
                print(await resp.text())
    except Exception as  error:
        print('proxy responded with an error ', error)


async def main():
    tasks = []
    with open(csvfile) as open_file:
        reader = csv.reader(open_file)
        for csv_row in reader:
            task = asyncio.create_task(chake_proxy(url_to_check,csv_row[0]))
            tasks.append(task)
    await asyncio.gather(*tasks)


asyncio.run(main())