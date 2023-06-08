# 개인정보 수집 유효기간
# 개인정보 수집 일자 "2022.05.19"
# A 유효기간 6달 B 유효기간 12달 C 유효기간 3달
# 유효기간 지난 파기해야할 개인정보는 result [1,3]
#
# 2023-06-08 start 07:37 - stop 08:20 not solved
# 2023-06-09 start 07:50 - stop 08:10 채점 : 25.0/100.0
#
from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    for (idx, i) in enumerate(privacies):
        sp = i.split(' ')
        date = sp[0]
        date_sp = date.split('.')
        date_y = int(date_sp[0])
        date_m = int(date_sp[1])
        date_d = int(date_sp[2])
        # print(i)
        target = sp[1]
        for (jdx, j) in enumerate(terms):
            if target in j:
                date_m = date_m + int(j.split(' ')[1])
                if date_m > 12:
                    date_y = date_y + 1
                    date_m = date_m % 12


        goal_format = '%Y.%m.%d'
        goal_date = f'{date_y}.{date_m}.{date_d}'
        goal = datetime.strptime(goal_date, goal_format)
        today_ = datetime.strptime(today, goal_format)
        # print(goal)
        # print(today_)
        if goal <= today_:
            # print('지남')
            answer.append(idx+1)
        # else:
            # print('안지남')


    print(answer)

    return answer

if __name__ == '__main__':
    solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
    solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])