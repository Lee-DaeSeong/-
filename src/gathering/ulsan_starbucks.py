import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def page_down():
    prev = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        cur = browser.execute_script("return document.body.scrollHeight")
        if cur == prev:
            break
        prev = cur

browser = webdriver.Chrome()
browser.maximize_window()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}

url = 'https://www.starbucks.co.kr/store/store_map.do?disp=locale'
browser.get(url)

(WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "울산")))).click()


gu_list = ["남구", "동구", "북구", "울주군", "중구"]

f = open("울산_스타벅스.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

for gu in gu_list:

    time.sleep(3)
    browser.find_element_by_link_text(gu).click()
    time.sleep(3)
    soup = BeautifulSoup(browser.page_source, "lxml")
    shops = soup.find_all("li", {"class": "quickResultLstCon"})

    for shop in shops:
        shop_name = shop["sales_data-name"]
        shop_address, none = str(shop.p).split('<br/>')
        shop_address = shop_address[shop_address.find('>') + 1:]
        # dong_remove=shop_address[:shop_address.find('(')]

        writer.writerow([gu, shop_name, shop_address])
        print(gu, shop_name, shop_address)

    # browser.find_element_by_link_text('지역 검색').click()
    browser.find_element_by_xpath('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/header[2]/h3/a').click()
    time.sleep(3)
    # browser.find_element_by_link_text('서울').click()
    browser.find_element_by_xpath('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[1]/a').click()

browser.quit()