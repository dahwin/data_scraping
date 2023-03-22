from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROXY = '18.235.55.193:8080'

opts = Options()
user_agent = 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'

webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True


opts.add_argument("user-agent="+user_agent)

print(webdriver.DesiredCapabilities.CHROME)

driver =webdriver.Chrome(r".\chromedriver.exe",options=opts)


driver.get("https://www.pinterest.com")

driver.get('https://www.pinterest.com')
user_agent_check = driver.execute_script("return navigator.userAgent;")
print(user_agent_check)