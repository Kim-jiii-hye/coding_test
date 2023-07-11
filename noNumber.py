# 최소 직사각형
#
# 2023-07-11 22:08 - 22:17
# 채점 : 100.0/100.0

def solution(numbers):
    check = [1,2,3,4,5,6,7,8,9]
    check_set = set(check)
    numbers_set = set(numbers)

    ans = check_set - numbers_set
    answer = sum(ans)
    print(answer)



if __name__ == '__main__':
    solution([1,2,3,4,6,7,8,0])
    solution([5,8,4,0,6,7,9])


