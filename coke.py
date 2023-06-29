# 콜라 문제
import math
# 2023-06-29 start 07:10 -

# 채점 : 0.0/100.0
def solution(a, b, n):
    # 빈병 20개 가져감 => 20/2 10병 모두 마심 => 10/2 5병 모두 => 5/2 2병 => 2병 /2 1병 => 남아있던 1병 까지
    # print(f"{n} - {for_mart} + {get_coke} = {have_coke}")
    # print(f"{for_mart} + {have_coke} - {n} = {get_coke}")

    get_coke = int(n / a)
    print(get_coke)
    get_coke = int(get_coke / a)
    print(get_coke)
    get_coke = int(get_coke / a)
    print(get_coke)

if __name__ == '__main__':
    # solution(2, 1, 20)
    solution(3, 1, 20)
