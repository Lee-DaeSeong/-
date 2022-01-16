import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://www.sbiz.or.kr/sup/main.do'
browser.get(url)

browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/ul/li[1]/a').click()

elem = browser.find_element_by_xpath('//*[@id="id"]')
elem.send_keys("dleotjd510")

elem = browser.find_element_by_xpath('//*[@id="pass"]')
elem.send_keys("N$WSB*Xw4FiGQDn")

browser.find_element_by_xpath('/html/body/div/div[3]/form/div/button').click()

f_read = open('울산.csv', 'r', encoding='utf-8')
rdr = csv.reader(f_read)

f = open("울산_상권분석.csv", "w", encoding="utf-8-sig", newline="")
csv_writer = csv.writer(f)

flag=True
def sb(line):
    try:
        time.sleep(3)
        browser.get('https://sg.sbiz.or.kr/godo/analysis.sg')
        global flag
        if flag:
            time.sleep(3)
            browser.find_element_by_xpath('//*[@id="help_guide"]/div/div[2]/div[1]/label').click()
            browser.find_element_by_link_text('닫기').click()
            flag = False
        time.sleep(3)

        element = browser.find_element_by_xpath('//*[@id="searchAddress"]')
        time.sleep(2)
        element.send_keys(line[2])
        time.sleep(2)
        element.send_keys(Keys.ENTER)
        # browser.execute_script("arguments[0].click();", element)

        # elem = browser.find_element_by_xpath('//*[@id="searchAddress"]')
        # elem.click()
        # time.sleep(2)
        # elem.send_keys(line[2]+'\n')
        # time.sleep(3)

        browser.find_element_by_link_text('확인').click()
        browser.find_element_by_xpath('//*[@id="icon-word1"]').click()
        time.sleep(3)
        for i in range(40):
            cur = '//*[@id="container"]/div[{}]/div/div[2]/div[2]/div[2]/div/ul/li[1]/div/ul/li[2]/label/span'.format(i)
            try:
                elem = browser.find_element_by_xpath(cur)
            except:
                continue
            if elem is not None:
                try:
                    elem.click()
                except:
                    sb(line)
        time.sleep(3)
        element = browser.find_element_by_xpath('//*[@id="checkTypeConfirm"]/span')
        time.sleep(2)
        browser.execute_script("arguments[0].click();", element)
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="map"]/div[1]/div/div[6]/div[2]/div/ul/li[1]/label/span').click()
        browser.find_element_by_xpath('//*[@id="map"]/div[1]/div/div[6]/div[2]/div/ul/li[1]/div/ul/li[2]/label').click()
        browser.find_element_by_xpath('//*[@id="auto_circle"]/div/div[2]/ul/li[2]/label').click()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="auto_circle"]/div/div[3]/a[2]/span').click()
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="map"]/div[1]/div/div[6]/div[3]/img').click()

        (WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.LINK_TEXT, "인구분석")))).click()
        time.sleep(3)
        soup = BeautifulSoup(browser.page_source, "lxml")

        page3 = soup.find("div", {"id": "page3"})
        tbodys = page3.find_all("tbody")

        result = list()

        weekend = list()
        for tbody in tbodys:

            if tbody.find("커피전문점/카페/다방") != "None":
                tds = tbody.find_all("td")
                for td in tds:
                    divs = td.find_all("div", {"class": "updown"})
                    # print(divs)
                    for div in divs:
                        # print(div.text.strip().replace(' ', '').replace('\n','').replace('\t',''))
                        result.append(div.text.strip().replace(' ', '').replace('\n', '').replace('\t', '').split('(')[0])

            if tbody.find("주중/주말") != "None":
                tds = tbody.find_all("td")
                weekend.append(tds)

        page4 = soup.find("div", {"id": "page4"})
        tbodys = page4.find_all("tbody")
        ingu = list()
        for tbody in tbodys:
            if tbody.find("<tr style=\"font-size:14px;") != "None":
                tds = tbody.find_all("td", {"class": "right"})
                for td in tds:
                    ingu.append(td.text.strip().replace(' ', '').replace('\n', '').replace('\t', '').replace(',', ''))

        csv_writer.writerow([line[1], line[2]])
        csv_writer.writerow(['영역', '구분', '21/03', '21/04', '21/05', '21/06', '21/07', '21/08'])
        csv_writer.writerow(['분석 영역', '매출액'] + result[12:18])
        csv_writer.writerow(['분석 영역', '건수'] + result[18:24])
        csv_writer.writerow(['유사 상권', '매출액'] + result[24:30])
        csv_writer.writerow(['유사 상권', '건수'] + result[30:36])

        for i in range(len(weekend[-3])):
            weekend[-3][i] = weekend[-3][i].text

        for i in range(len(weekend[-2])):
            weekend[-2][i] = weekend[-2][i].text

        for i in range(len(weekend[-1])):
            weekend[-1][i] = weekend[-1][i].text

        # 주중/주말, 요일별 병균 매출
        csv_writer.writerow(['영역', '구분', '주중', '주말', '월', '화', '수', '목', '금', '토', '일'])

        csv_writer.writerow(['분석 영역', '매출액'] + weekend[-3][:9])
        csv_writer.writerow(['분석 영역', '비율'] + weekend[-3][9:])

        # 시간대별 월 평균 매출
        csv_writer.writerow(['영역', '구분', '00~06시', '06~11시', '11~14시', '14~17시', '17~21시', '21~24시'])
        csv_writer.writerow(['분석 영역', '매출액'] + weekend[-2][:6])
        csv_writer.writerow(['분석 영역', '비율'] + weekend[-2][6:])

        # 연령대별 월 평균 매출
        csv_writer.writerow(['영역', '구분', '남성', '여성', '10대', '20대', '30대', '40대', '50대', '60대 이상'])
        csv_writer.writerow(['분석 영역', '매출액'] + weekend[-1][:8])
        csv_writer.writerow(['분석 영역', '비율'] + weekend[-1][8:])

        # 월별 일 평균 유동 인구
        csv_writer.writerow(
            ['구분', '구분', '20/08', '20/09', '20/10', '20/11', '20/12', '21/01', '21/02', '21/03', '21/04', '21/05', '21/06',
             '21/07', '21/08'])
        csv_writer.writerow(['분석 영역', '유동 인구'] + ingu[:13])
        csv_writer.writerow(['분석 영역', '증감율', '0'] + ingu[13:25])
    except:
        sb(line)
        print(line)

i=0
for line in rdr:
    i+=1
    print(i)
    sb(line)

f_read.close()
f.close()
browser.quit()

