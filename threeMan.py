# 삼총사 문제

# 2023-07-02 start 11:48 - stop 12:06
# 3명 합쳐서 0이 되도록
import itertools

# 채점 : 0/100.0
def solution(number):
    answer = 0
    per = list(itertools.combinations(number, 3))
    for ele in per:
        print(f"ele:{ele} sum:{sum(ele)}")
        if sum(ele) == 0:
            answer = answer + 1
    print(answer)

if __name__ == '__main__':
    solution([-2, 3, 0, 2, -5])
    solution([-3, -2, -1, 0, 1, 2, 3])
    solution([-1, 1, -1, 1])

