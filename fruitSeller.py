# 과일 장수

# 2023-06-20 start 22:00 - stop

# 채점 : 100.0/100.0
from itertools import permutations
def solution(k, m, score):
    box_res = []

    # 최솟값보다 큰 값
    box = []
    for i in score:
        if len(box) < m:
            if min(score) < i:
                box.append(i)

        if box not in box_res:
            box_res.append(box)

    # print(box_res)
    min_app = min(box_res[0])
    one_box = m
    box_cnt = len(box_res)
    res = min_app * one_box * box_cnt
    print(res)

if __name__ == '__main__':
    solution(3, 4, [1,2,3,1,2,3,1])
    # solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])

