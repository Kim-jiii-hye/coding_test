# 기사 단원의 무기

# 2023-06-19 start 07:10 - stop 07:28

# 채점 : 66.7/100.0

def solution(number, limit, power):
    answer = 0
    # number의 약수
    number_list = list(range(1,number+1))
    cnt_list = []
    for i in number_list:
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt = cnt + 1
        cnt_list.append(cnt)
    print(cnt_list)
    for c in cnt_list:
        if c <= limit:
            answer = answer + c
        else:
            c = power
            answer = answer + c
    print(answer)





if __name__ == '__main__':
    solution(5, 3, 2)
    solution(10, 3, 2)
