# 콜라 문제
import math
# 2023-06-29 start 07:10 - 07:40
# 2023-06-30 start 07:10 - 07:40
# 2023-07-01 start 13:40 - 14:05

# 채점 : 7.1/100.0
def solution(a, b, n):
    # 빈병 20개 가져감 => 20/2 10병 모두 마심 => 10/2 5병 모두 => 5/2 2병 => 2병 /2 1병 => 남아있던 1병 까지
    get_coke = int((n / a) * b)
    answer = get_coke
    while(get_coke > 1):
        get_coke = (get_coke / a) * b
        print(get_coke)
        answer = answer + get_coke
    print(round(answer))

if __name__ == '__main__':
    solution(2, 1, 20)
    solution(3, 1, 20)
