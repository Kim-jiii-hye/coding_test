# 약수의 개수와 덧셈

# 2023-07-14 08:48 - 08:57

# 채점 : 100.0/100.0
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        measure = 0
        for j in range(1, i + 1):
            if (i % j == 0):
                # print(j)
                measure = measure + 1
        # print(measure)
        if measure % 2 != 0:
            answer = answer - i
        else:
            answer = answer + i
    print(answer)


if __name__ == '__main__':
    solution(13, 17)
    solution(24, 27)
