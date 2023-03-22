import csv
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option("detach", True)
# Open the CSV file
with open('active_proxies.csv', 'r') as f:
    # Create a CSV reader
    reader = csv.reader(f)

    # Loop through the proxies
    for row in reader:
        proxy = row[0]

        # Set the desired capabilities
        desired_capabilities = DesiredCapabilities.CHROME

        # Set the proxy
        desired_capabilities['proxy'] = {
            "httpsProxy":proxy,
            "httpProxy": proxy,
            "ftpProxy": proxy,
            "sslProxy": proxy,
            "noProxy": None,
            "proxyType": "MANUAL",
            "class": "org.openqa.selenium.Proxy",
            "autodetect": False
        }

        # Create the driver with the desired capabilities
        driver = webdriver.Chrome(desired_capabilities=desired_capabilities,options=options)
        # driver.get("https://www.flipkart.com/search?q=watch&sid=r18%2Cf13&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=watch%7CWrist+Watches&requestId=d64659cc-2125-411f-bd7a-2d09b895305b")
        driver.get('https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-100.8130476846494%2C%22east%22%3A-94.3860457315244%2C%22south%22%3A30.90367419298664%2C%22north%22%3A34.65267485567684%7D%2C%22mapZoom%22%3A8%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D')

        # Your code to perform web scraping using the driver goes here

        # Close the driver
