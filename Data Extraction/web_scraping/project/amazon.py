from requests_html import HTMLSession

url = 'https://www.youtube.com'
s = HTMLSession()
r = s.get(url)
r.html.render(sleep=1,timeout=20)
print(r.status_code)


