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

(WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "서울")))).click()

gu_list = ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구",
            "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구",
            "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"]
# gu_list = ["남구", "동구", "북구", "울주군", "중구"]

seoul_f = open("서울.csv", "w", encoding="utf-8-sig", newline="")
seoul_writer = csv.writer(seoul_f)
actions=ActionChains(browser)

for gu in gu_list:
    cur_f=open("{}.csv".format(gu), "w", encoding="utf-8-sig", newline="")
    cur_writer=csv.writer(cur_f)

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

        seoul_writer.writerow([gu, shop_name, shop_address])
        cur_writer.writerow([gu, shop_name, shop_address])
        print(gu, shop_name, shop_address)
    browser.execute_script('window.scrollTo(0,0)')
    # browser.find_element_by_link_text('지역 검색').click()
    browser.find_element_by_xpath('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/header[2]/h3/a').click()
    time.sleep(3)
    # browser.find_element_by_link_text('서울').click()
    browser.find_element_by_xpath('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[1]/a').click()

browser.quit()