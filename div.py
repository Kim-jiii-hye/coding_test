# 나머지가 1이 되는 수 찾기
#
# 2023-07-09 20:45 -
# 채점 : 20.0/100.0

def solution(n):
    res = []
    # n의 약수
    for i in range(1, n+1):
        if n % i != 0:
            res.append(i)
    print(res)
    ans = []
    for i in res:
        if n % i == 1:
            ans.append(i)
    answer = min(ans)
    print(answer)


if __name__ == '__main__':
    solution(10)
    solution(12)


