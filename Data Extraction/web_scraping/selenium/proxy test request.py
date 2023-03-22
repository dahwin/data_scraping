#
# import csv
# import asyncio
# import aiohttp
#
# async def check_proxy(session, proxy):
#     try:
#         async with session.get('https://www.inmyarea.com/utilities?zipcode=50166', proxy=f"http://{proxy}") as response:
#             if response.status == 200:
#                 return proxy
#     except:
#         pass
#     return None
#
# async def main():
#     # List of proxies to test
#     proxies = []
#     with open('http.csv', 'r') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             proxies.append(row[0])
#
#     # Test each proxy and save the active ones to a list
#     active_proxies = []
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for proxy in proxies:
#             task = asyncio.create_task(check_proxy(session, proxy))
#             tasks.append(task)
#
#         for task in asyncio.as_completed(tasks):
#             result = await task
#             if result:
#                 active_proxies.append(result)
#
#     # Save the active proxies to a CSV file
#     with open('active_proxies.csv', 'w', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(['Proxy'])
#         for proxy in active_proxies:
#             writer.writerow([proxy])
#
# asyncio.run(main())

import csv
import asyncio
import aiohttp

async def check_proxy(session, proxy):
    try:
        async with session.get('https://www.flipkart.com/search?q=watch&sid=r18%2Cf13&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=watch%7CWrist+Watches&requestId=d64659cc-2125-411f-bd7a-2d09b895305b', proxy=f"http://{proxy}") as response:
            if response.status == 200:
                return proxy
    except:
        pass
    return None

async def main():
    # List of proxies to test
    proxies = []
    with open('http.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            proxies.append(row[0])

    # Test each proxy and save the active ones to a list
    active_proxies = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for proxy in proxies:
            task = asyncio.create_task(check_proxy(session, proxy))
            tasks.append(task)

        for task in asyncio.as_completed(tasks):
            result = await task
            if result:
                active_proxies.append(result)

    # Save the active proxies to a CSV file
    with open('active_proxies.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Proxy'])
        for proxy in active_proxies:
            writer.writerow([proxy])

asyncio.run(main())


