import csv
import numpy as np
f = open("서울_평균.csv", 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
rdr = list(rdr)

f = open("서울_결과.csv", 'w', encoding='utf-8-sig', newline="")
csv_writer = csv.writer(f)

csv_writer.writerow(['해당 구 스타벅스 평균 - 해당 구 전체 평균'])
csv_writer.writerow(['지역', '21.04', '21.05', '21.06', '21.07', '21.08', '21.09'])
seoul_mean_diff=[]
seoul_cnt_diff=[]
cnt=0

a=[]
b=[]
for i in range(len(rdr)):
    if len(rdr[i])==1:
        csv_writer.writerow(rdr[i])

        sb_mean=np.array(rdr[i+1][1:], dtype='int64')
        gu_mean=np.array(rdr[i+3][1:], dtype='int64')

        sb_cnt=np.array(rdr[i+2][1:], dtype='int64')
        gu_cnt=np.array(rdr[i+4][1:], dtype='int64')

        csv_writer.writerow(['평균 매출액 차이'] + list(sb_mean-gu_mean))
        csv_writer.writerow(['평균 건수 차이'] + list(sb_cnt-gu_cnt))

        seoul_mean_diff.append(sb_mean - gu_mean)
        seoul_cnt_diff.append(sb_cnt - gu_cnt)

        a.append(list(sb_mean))
        b.append(list(sb_cnt))

seoul_mean_diff=np.array(seoul_mean_diff)
seoul_cnt_diff=np.array(seoul_cnt_diff)

a=np.array(a)
b=np.array(b)


csv_writer.writerow(['서울'])
csv_writer.writerow(['평균 매출액 차이'] + list(np.sum(seoul_mean_diff, axis=0) // len(seoul_mean_diff)))
csv_writer.writerow(['평균 건수 차이'] + list(np.sum(seoul_cnt_diff, axis=0) // len(seoul_cnt_diff)))
csv_writer.writerow(['서울 스벅 평균 매출'] + list(np.sum(a, axis=0)//len(a)))
csv_writer.writerow(['서울 스벅 평균 건수'] + list(np.sum(b, axis=0)//len(b)))
csv_writer.writerow(['서울 전체 평균 매출'] + ['1322', '1348', '1339', '1280', '1222', '1298'])
csv_writer.writerow(['서울 전체 평균 건수'] + ['1874', '1910', '1895', '1877', '1779', '1856'])
csv_writer.writerow(['서울 스벅 평균 매출 - 서울 전체 평균 매출'] + list(np.sum(a, axis=0)//len(a) - np.array([1322, 1348, 1339, 1280, 1222, 1298])))
csv_writer.writerow(['서울 스벅 평균 건수 - 서울 전체 평균 건수'] + list(np.sum(b, axis=0)//len(b) - np.array([1874, 1910, 1895, 1877, 1779, 1856])))
