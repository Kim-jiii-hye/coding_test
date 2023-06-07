# 개인정보 수집 유효기간
# 개인정보 수집 일자 "2022.05.19"
# A 유효기간 6달 B 유효기간 12달 C 유효기간 3달
# 유효기간 지난 파기해야할 개인정보는 result [1,3]
#
# 2023-06-08 start 07:37 - stop
# 채점 : 0.0/100.0\
from datetime import datetime, timedelta

def solution(today, terms, privacies):
    answer = []
    for i in privacies:
        sp = i.split(' ')
        date_origin = sp[0]
        date_format = '%Y.%m.%d'
        date = datetime.strptime(date_origin, date_format)
        target = sp[1]
        print(f"날짜:{date}")
        # 한 달에 28일 씩 6달
        for (jdx,j) in enumerate(terms):
            if target in j:
                target_month = int(j.split(' ')[1])
                tar_m = date.month
                tar_y = date.year
                tar_d = date.day
                res_m = tar_m + target_month
                print(res_m)

                result = f"{tar_y}.{res_m}.{tar_d}"

                print(result)
                print(today)
                # if today_date >= result:
                #     print(f"")
            else:
                continue




    return answer

if __name__ == '__main__':
    solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
    solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])