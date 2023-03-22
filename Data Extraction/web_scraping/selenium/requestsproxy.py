import csv
import random
import requests
from bs4 import BeautifulSoup
# Read in the proxy list from the CSV file
proxy_list = []

with open('qproxy.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    proxy_list.append(row[0])

# Set the URL you want to scrape
# url = 'https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#your-proxy-appears-to-only-use-http-and-not-https'
url = 'https://whoer.net/'

# Set the user agent for the request
user_agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36)'

# Set the headers for the request
headers = {'User-Agent': user_agent}

# Set the number of times to rotate the proxy
num_rotations = 1

# Rotate the proxy num_rotations times
for i in range(num_rotations):
  # Choose a random proxy from the list
  proxy = random.choice(proxy_list)

  # Set the proxy for the request
  proxies = {'https': proxy, 'http': proxy}

  # Send the request
  response = requests.get(url, headers=headers, proxies=proxies,verify=False)
  soup = BeautifulSoup(response.content,'lxml')

  # Print the response
  print(soup.prettify())

