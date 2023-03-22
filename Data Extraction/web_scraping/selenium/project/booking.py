'''dahyun+darwin = dahwin'''
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

data = []
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.booking.com/searchresults.en-gb.html?ss=Seoul&ssne=Seoul&ssne_untouched=Seoul&label=booking-name-IquAp*EbiLS6jPVl_he8yQS461500239787%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9074041%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YYriJK-Ikd_dLBPOo0BdMww&sid=43cfe5fcf219e687da9f6f83ea54ab60&aid=378266&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-716583&dest_type=city&checkin=2023-02-04&checkout=2023-02-05&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure')
# driver.get('https://www.booking.com/searchresults.en-gb.html?ss=Gyeonggi-do%2C+South+Korea&ssne=Seoul&ssne_untouched=Seoul&label=booking-name-IquAp*EbiLS6jPVl_he8yQS461500239787%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9074041%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YYriJK-Ikd_dLBPOo0BdMww&sid=43cfe5fcf219e687da9f6f83ea54ab60&aid=378266&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=3935&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=382a46132aae02fe&ac_meta=GhAzODJhNDYxMzJhYWUwMmZlIAAoATICZW46C0d5ZW9uZ2dpLWRvQABKAFAA&checkin=2022-12-27&checkout=2022-12-28&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure')
isNextDisabled = False
while not isNextDisabled:
    try:
        element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.d20f4628d0')))

        booking = driver.find_element(By.CSS_SELECTOR,'#search_results_table > div:nth-child(2) > div > div > div')
        div = booking.find_elements(By.CSS_SELECTOR,'div.d20f4628d0')
        for info in div:
            name = info.find_element(By.CSS_SELECTOR,'div.fcab3ed991.a23c043802').text
            try:
                first_price = info.find_element(By.CSS_SELECTOR, 'span.c5888af24f.e729ed5ab6').text
            except:
                first_price= None
            try:
                price = info.find_element(By.CSS_SELECTOR,'span.fcab3ed991.fbd1d3018c.e729ed5ab6').text
            except:
                price = None

            try:
                away_from_center = info.find_element(By.CSS_SELECTOR,'[data-testid="distance"]').text
            except:
                away_from_center = None
            try:
                type = info.find_element(By.CSS_SELECTOR,'div.b5cd09854e.f0d4d6a2f5.e46e88563a').text
            except:
                type = None
            try:
                rating = info.find_element(By.CSS_SELECTOR,'.b5cd09854e.d10a6220b4').text
            except:
                rating = None
            try:
                reviews = info.find_element(By.CSS_SELECTOR,'.d8eab2cf7f.c90c0a70d3.db63693c62').text
            except:
                reviews = None


            d ={
               "Name":name,
                "First_Price":first_price,
                'Price':price,
                'Away From Center':away_from_center,
                'Type':type,
                'Rating':rating,
                'Reviews':reviews
            }
            data.append(d)
            print(d)
        next_b = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button.fc63351294')))
        next_clas = next_b.get_attribute("disabled")

        if next_clas is True:
            isNextDisabled = True
        else:
            driver.find_element(By.CSS_SELECTOR,'div.f32a99c8d1.f78c3700d2').click()
            driver.refresh()
    except Exception as e:
        print(e,'Main Error')
        isNextDisabled = True

print(data)
print(len(data))
import pandas
df = pandas.DataFrame(data)
df.to_csv('dahwin3.csv')
