
import csv
# def get_proxies():
#     proxies = []
#     with open('active_proxies.csv') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             # Add a default scheme to the proxy URL based on the type of proxy
#             if "socks4" in row[0]:
#                 proxy = "socks4://" + row[0]
#             elif "socks5" in row[0]:
#                 proxy = "socks5://" + row[0]
#             elif "https" in row[0]:
#                 proxy = "https://" + row[0]
#             else:
#                 proxy = "http://" + row[0]
#             proxies.append(proxy)
#     return proxies
import aiohttp
from bs4 import BeautifulSoup
import asyncio
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://www.youtube.com/@TWICE/videos',proxy='http://148.72.246.227:9453') as response:
#             print("Status:", response.status)
#             print("Content-type:", response.headers['content-type'])
#
#             html = await response.text()
#             print("Body:", html, "...")
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


