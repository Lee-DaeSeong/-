import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'https://golmok.seoul.go.kr/regionAreaAnalysis.do'
driver = webdriver.Chrome() # webdriver 실행(크롬 창 생성)
driver.maximize_window()

driver.get(url)

driver.find_element_by_xpath('//*[@id="loginPop"]/div/button[1]').click() # 비회원 로그인

# 검색 조건 설정
year = '//*[@id="selectYear"]/option[1]'
driver.find_element_by_xpath(year).click() # 년
time.sleep(1)
past = '//*[@id="selectQuCondition"]/option[2]' #전분기
driver.find_element_by_xpath(past).click()
time.sleep(1)
semester = '//*[@id="selectQu"]/option[4]'
driver.find_element_by_xpath(semester).click() # 분기
time.sleep(1)


driver.find_element_by_xpath('//*[@id="induL"]/option[2]').click() # 외식업
time.sleep(1)

driver.find_element_by_xpath('//*[@id="induM"]/option[11]').click() # 커피/음료
time.sleep(1)

driver.find_element_by_xpath('//*[@id="infoCategory"]/option[3]').click() # 점포수
time.sleep(1)

driver.find_element_by_xpath('//*[@id="presentSearch"]').click() # 검사 버튼
time.sleep(1)

soup = BeautifulSoup(driver.page_source, "lxml")
gu_list = soup.find_all('tr',{'class':'branch collapsed'})

for gu in gu_list:

    tds = gu.find_all('td')
    data=[]
    data.append(tds[0].text.replace(' ',''))
    tds.pop(0)

    tds.pop(0)

    for td in tds:
        data.append(td.text.replace(',',''))

    print(data[-1])

# print(soup)


driver.quit()