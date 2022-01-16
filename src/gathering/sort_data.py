import csv
import numpy as np
from collections import OrderedDict

f = open("서울_평균.csv", "r", encoding="utf-8-sig", newline="")
rdr = csv.reader(f)
rdr=list(rdr)

sb_mean_dic={}
gu_mean_dic={}

sb_cnt_dic={}
gu_cnt_dic={}

for i in range(len(rdr)):
    if len(rdr[i])==1:
        # sb_mean_dic[(rdr[i][0])] = [(sum(list(map(int, rdr[i+1][1:])))//6), (sum(list(map(int, rdr[i+2][1:])))//6)]
        sb_mean_dic[(rdr[i][0])] = (sum(list(map(int, rdr[i+1][1:])))//6)
        gu_mean_dic[(rdr[i][0])] = (sum(list(map(int, rdr[i+3][1:])))//6)

        sb_cnt_dic[rdr[i][0]]= (sum(list(map(int, rdr[i+2][1:])))//6)
        gu_cnt_dic[(rdr[i][0])]= (sum(list(map(int, rdr[i+4][1:])))//6)

orderd_sb_mean_dic=OrderedDict(sorted(sb_mean_dic.items(), key=lambda x: x[1], reverse=True))
orderd_sb_cnt_dic=OrderedDict(sorted(sb_cnt_dic.items(), key=lambda x: x[1], reverse=True))
orderd_gu_mean_dic=OrderedDict(sorted(gu_mean_dic.items(), key=lambda x: x[1], reverse=True))
orderd_gu_cnt_dic=OrderedDict(sorted(gu_cnt_dic.items(), key=lambda x: x[1], reverse=True))


f = open("서울_정렬.csv", "w", encoding="utf-8-sig", newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(['스타벅스 상권 평균 매출 (21.04~21.09 평균)'])
for gu, data in orderd_sb_mean_dic.items():
    csv_writer.writerow([gu, data])
csv_writer.writerow(['스타벅스 상권 평균 건수 (21.04~21.09 평균)'])
for gu, data in orderd_sb_cnt_dic.items():
    csv_writer.writerow([gu, data])
csv_writer.writerow(['구 전체 평균 매출 (21.04~21.09 평균)'])
for gu, data in orderd_gu_mean_dic.items():
    csv_writer.writerow([gu, data])
csv_writer.writerow(['구 전체 평균 건수 (21.04~21.09 평균)'])
for gu, data in orderd_gu_mean_dic.items():
    csv_writer.writerow([gu, data])

f = open("울산_평균.csv", "r", encoding="utf-8-sig", newline="")
rdr = csv.reader(f)
rdr=list(rdr)

sb_mean_dic={}
gu_mean_dic={}

sb_cnt_dic={}
gu_cnt_dic={}

for i in range(len(rdr)):
    if len(rdr[i])==1:
        sb_mean_dic[(rdr[i][0])] = (sum(list(map(int, rdr[i+1][1:])))//6)
        gu_mean_dic[(rdr[i][0])] = (sum(list(map(int, rdr[i+3][1:])))//6)

        sb_cnt_dic[rdr[i][0]]= (sum(list(map(int, rdr[i+2][1:])))//6)
        gu_cnt_dic[(rdr[i][0])]= (sum(list(map(int, rdr[i+4][1:])))//6)

orderd_sb_mean_dic=OrderedDict(sorted(sb_mean_dic.items(), key=lambda x: x[1], reverse=True))
orderd_sb_cnt_dic=OrderedDict(sorted(sb_cnt_dic.items(), key=lambda x: x[1], reverse=True))
orderd_gu_mean_dic=OrderedDict(sorted(gu_mean_dic.items(), key=lambda x: x[1], reverse=True))
orderd_gu_cnt_dic=OrderedDict(sorted(gu_cnt_dic.items(), key=lambda x: x[1], reverse=True))

f = open("울산_정렬.csv", "w", encoding="utf-8-sig", newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(['스타벅스 상권 평균 매출 (21.04~21.09 평균)'])
for gu, data in orderd_sb_mean_dic.items():
    csv_writer.writerow([gu, data])
csv_writer.writerow(['스타벅스 상권 평균 건수 (21.04~21.09 평균)'])
for gu, data in orderd_sb_cnt_dic.items():
    csv_writer.writerow([gu, data])
csv_writer.writerow(['구 전체 평균 매출 (21.04~21.09 평균)'])
for gu, data in orderd_gu_mean_dic.items():
    csv_writer.writerow([gu, data])
csv_writer.writerow(['구 전체 평균 건수 (21.04~21.09 평균)'])
for gu, data in orderd_gu_mean_dic.items():
    csv_writer.writerow([gu, data])