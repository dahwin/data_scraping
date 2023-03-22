import time
from requests_html import HTMLSession

def infinite_scraper(url):
    session = HTMLSession()
    while True:
        r = session.get(url)
        # Scrape the data from the current page
        content = r.html.find("#mw-content-text", first=True)
        print(content.text)

        # Find the first Wikipedia link on the page
        next_link = r.html.find("a[href^='/wiki/']", first=True)

        # If there's a next link, follow it
        if next_link:
            url = "https://en.wikipedia.org" + next_link.attrs["href"]
        # If not, wait 5 seconds and start over at the original URL
        else:
            time.sleep(5)

if __name__ == "__main__":
    infinite_scraper("https://en.wikipedia.org/wiki/Colin_Robert_Chase")
