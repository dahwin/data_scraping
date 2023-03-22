import csv
import aiohttp
import asyncio
from bs4 import BeautifulSoup

# Read in the CSV file and extract the list of URLs
urls = []
with open('40000.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        url = row[0]
        urls.append(url)


# Define a function to get the full URL for a relative URL
def get_full_url(base_url, url):
    if url.startswith('http'):
        return url
    else:
        return base_url + url


# Define a function to scrape the data from a given URL
async def scrape_data(session, base_url, url):
    # Get the full URL for the relative URL
    full_url = get_full_url(base_url, url)

    # Send an HTTP request to the URL asynchronously
    async with session.get(full_url) as response:
        # Extract the data using Beautiful Soup
        soup = BeautifulSoup(await response.text(), 'html.parser')
        data = soup.select('.provider-name a')

        return data


async def main():
    # Create an aiohttp client session
    async with aiohttp.ClientSession() as session:
        # Use asyncio.as_completed to iterate over the tasks as they are completed
        tasks = [scrape_data(session, 'https://www.inmyarea.com/utilities?zipcode=63301', url) for url in urls]
        for task in asyncio.as_completed(tasks):
            data = await task
            print(data)


# Run the main function
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
