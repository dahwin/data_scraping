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
        async with session.get('https://lottiefiles.com/animations/animations/business-people-shaking-hands-c6S2KwlSjQ', proxy=f"http://{proxy}") as response:
            if response.status == 200:
                return proxy
    except:
        pass
    return None

async def main():
    # List of proxies to test
    proxies = []
    with open('proxy.csv', 'r') as f:
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


