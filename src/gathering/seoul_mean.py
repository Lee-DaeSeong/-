import csv
import numpy as np


gu_list = ["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구",
            "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구",
            "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"]

mean_f = open("sales_data/서울_구_평균매출.txt", 'r', encoding='utf-8-sig')
mean_lines = mean_f.readlines()

idx=0


res_f = open("서울_평균.csv", "w", encoding="utf-8-sig", newline="")
csv_writer = csv.writer(res_f)

sales_res_arr=[]
cnt_res_arr=[]

for gu in gu_list:
    f = open("./sales_data/{}_상권분석.csv".format(gu), "r", encoding="utf-8-sig", newline="")
    reader = csv.reader(f)
    i=0
    res=0
    cnt=0
    sales_arr=[]
    cnt_arr=[]

    for r in reader:
        i+=1
        if i==3:
            cnt+=1
            data = r
            data.pop(0)
            data.pop(0)
            data=[int(x.replace(',','')) for x in data]
            if len(data)==0:
                continue
            sales_arr.append(data)
        if i==4:
            data = r
            data.pop(0)
            data.pop(0)
            data=[int(x.replace(',','')) for x in data]

            if len(data)==0:
                continue

            cnt_arr.append(data)

        if i==18:
            i=0

    sales_arr=np.array(sales_arr)
    cnt_arr=np.array(cnt_arr)

    print(gu)
    # print(np.sum(sales_arr, axis=0)//cnt)
    # print(np.sum(cnt_arr, axis=0)//cnt)

    csv_writer.writerow([gu])
    csv_writer.writerow(['스타벅스 평균 매출액'] + list(np.sum(sales_arr, axis=0)//cnt))
    csv_writer.writerow(['스타벅스 평균 건수'] + list(np.sum(cnt_arr, axis=0)//cnt))

    temp = mean_lines[idx].split(' ')
    temp[-1] = temp[-1].replace('\n', '')
    temp.pop(0)

    csv_writer.writerow(['{} 평균 매출액'.format(gu)] + temp)

    idx+=1
    temp = mean_lines[idx].split(' ')
    temp[-1] = temp[-1].replace('\n', '')
    temp.pop(0)

    csv_writer.writerow(['{} 평균 건수'.format(gu)] + temp)
    idx+=1

    f.close()

mean_f.close()
res_f.close()