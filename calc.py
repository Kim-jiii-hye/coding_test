# 부족한 금액 계산하기

# 2023-07-12 start 07:11 - 07:18

# 채점 : 100.0/100.0
def solution(price, money, count):
    calc = 0
    for i in range(1, count+1):
        calc = calc + (price * i)
    answer = calc - money
    if answer < 0:
        answer = 0
    return answer



if __name__ == '__main__':
    solution(3, 20, 4)
