import requests
from bs4 import BeautifulSoup

# Send a HTTP request to the Instagram post URL and retrieve the HTML content
url = "https://www.instagram.com/reel/ClGfGG_gN5Q/"
response = requests.get(url)
html_content = response.text

# Parse the HTML content and extract the direct link of the video
soup = BeautifulSoup(html_content, 'html.parser')
script_element = soup.find('script', {'type': 'text/javascript'})
video_url = script_element.text.split('video_url":"')[1].split('","video_view_count')[0]

print(video_url)
