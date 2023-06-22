# 햄버거 만들기

# 2023-06-23 start 07:15 - 07:35

# 채점 : 33.3/100.0
def solution(ingredient):
    answer = 0
    res = [1,2,3]
    for (idx,i) in enumerate(ingredient):
        hamburger = []
        if i == 1:
            if idx+1 < len(ingredient) and idx+2 < len(ingredient):
                hamburger.append(ingredient[idx])
                hamburger.append(ingredient[idx + 1])
                hamburger.append(ingredient[idx + 2])

        if hamburger == res:
            answer = answer + 1
    print(answer)


if __name__ == '__main__':
    solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
    solution([1, 3, 2, 1, 2, 1, 3, 1, 2])