import csv
import numpy as np
f = open("울산_평균.csv", 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
rdr = list(rdr)

f = open("울산_결과.csv", 'w', encoding='utf-8-sig', newline="")
csv_writer = csv.writer(f)

csv_writer.writerow(['해당 구 스타벅스 평균 - 해당 구 전체 평균'])
csv_writer.writerow(['지역', '21.04', '21.05', '21.06', '21.07', '21.08', '21.09'])
ulsan_mean_diff=[]
ulsan_cnt_diff=[]
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

        ulsan_mean_diff.append(sb_mean - gu_mean)
        ulsan_cnt_diff.append(sb_cnt - gu_cnt)

        a.append(list(sb_mean))
        b.append(list(sb_cnt))

ulsan_mean_diff=np.array(ulsan_mean_diff)
ulsan_cnt_diff=np.array(ulsan_cnt_diff)

a=np.array(a)
b=np.array(b)


csv_writer.writerow(['울산'])
csv_writer.writerow(['평균 매출액 차이'] + list(np.sum(ulsan_mean_diff, axis=0) // len(ulsan_mean_diff)))
csv_writer.writerow(['평균 건수 차이'] + list(np.sum(ulsan_cnt_diff, axis=0) // len(ulsan_cnt_diff)))
csv_writer.writerow(['울산 스벅 평균 매출'] + list(np.sum(a, axis=0)//len(a)))
csv_writer.writerow(['울산 스벅 평균 건수'] + list(np.sum(b, axis=0)//len(b)))
csv_writer.writerow(['울산 전체 평균 매출'] + ['791', '892', '927', '1009', '1000', '988'])
csv_writer.writerow(['울산 전체 평균 건수'] + ['915', '1023', '1009', '1097', '1098', '1109'])
csv_writer.writerow(['울산 스벅 평균 매출 - 울산 전체 평균 매출'] + list(np.sum(a, axis=0)//len(a) - np.array([791, 892, 927, 1009, 1000, 988])))
csv_writer.writerow(['울산 스벅 평균 건수 - 울산 전체 평균 건수'] + list(np.sum(b, axis=0)//len(b) - np.array([915, 1023, 1009, 1097, 1098, 1109])))
