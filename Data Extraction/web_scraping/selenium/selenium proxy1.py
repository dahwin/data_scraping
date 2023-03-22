from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# Set proxy URL and port
proxy_url = 'https://149.129.213.200:8080'

# Create a proxy object
proxy = Proxy()

# Set the proxy type to manual
proxy.proxy_type = ProxyType.MANUAL

# Set the HTTP and SSL proxy
proxy.http_proxy = proxy_url
proxy.ssl_proxy = proxy_url

# Add the proxy to the Chrome browser capabilities
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

# Create a Chrome browser instance with the desired capabilities
driver = webdriver.Chrome('G:/chromedriver.exe',
    desired_capabilities=capabilities
)

# Navigate to the website
driver.get('https://whoer.net/')
