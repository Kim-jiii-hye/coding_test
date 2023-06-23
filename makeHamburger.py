# 햄버거 만들기

# 2023-06-23 start 07:15 - 07:35

# 채점 : 33.3/100.0
def solution(ingredient):
    answer = 0
    check_res = [1,2, 3,1]
    cnt = []

    for (idx,i) in enumerate(ingredient):
        if i == 1:
            cnt.append(idx)
    print(f"cnt:{cnt}")
    print(f"ing:{ingredient}")
    for (jdx, j) in enumerate(cnt):
        if (jdx+1 < len(cnt)):
            print(f"{ingredient[j]}-{ingredient[j+1]}-{ingredient[j+2]}-{ingredient[j+3]}")





    print(answer)

if __name__ == '__main__':
    solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
    # solution([1, 3, 2, 1, 2, 1, 3, 1, 2])
    solution([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1])  #반례 테스트 추가