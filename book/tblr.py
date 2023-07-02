# 예제4-1 상하좌우

# 2023-07-03 start 07:18 -


# 채점 : 45.0/100.0
def solution(n, move):
    # n = 5x5
    start = [1, 1]
    for i in move:
        if i == "R":
            replace = start[1] + 1
            if replace > 0:
                start[1] = replace
        elif i == "L":
            replace = start[1] - 1
            if replace > 0:
                start[1] = replace
        elif i == "U":
            replace = start[0] - 1
            if replace > 0:
                start[0] = replace
        elif i == "D":
            replace = start[0] + 1
            if replace > 0:
                start[0] = replace
    rep = list(map(str, start))
    print(' '.join(rep))
    return ' '.join(rep)


if __name__ == '__main__':
    solution(5, ["R","R","R","U","D","D"])
