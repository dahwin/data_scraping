import requests

r = requests.get('https://www.amazon.com/s?k=laptop&i=computers&crid=27GFGJVF4KNRP&sprefix=%2Ccomputers%2C725&ref=nb_sb_ss_recent_1_0_recent')

print(r.status_code)