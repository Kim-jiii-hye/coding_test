# 과일 장수

# 2023-06-20 start 22:00 - stop 23:35
# 2023-06-21 start 22:00 - stop 23:04

# 채점 : 100.0/100.0
def solution(k, m, score):
    # 최솟값보다 큰 값
    box = []
    sort_score = sorted(score, reverse=True)

    for i in range(0, len(sort_score), m):

        arr = sort_score[i:i + m]
        box.append(arr)

    print(box)
    answer = 0

    for j in box:
        if len(j) == m:
            min_ap = min(j)
            # print(f"{min_ap} * {m}")
            res = min_ap * m
            answer = answer + res
    print(answer)




if __name__ == '__main__':
    solution(3, 4, [1,2,3,1,2,3,1])
    solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])

