import requests
from bs4 import BeautifulSoup

# URL of the web page
url = "https://deepmind.google/discover/blog/transforming-the-future-of-music-creation/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all text from the page
    all_text = soup.get_text()

    # Replace consecutive newlines with a single newline
    cleaned_text = '\n'.join(line.strip() for line in all_text.splitlines() if line.strip())

    # Print the cleaned text
    print(cleaned_text)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")


