# 덧칠하기
# n=>8(총 칠해야할 칸) m=>4(롤러의 길이) section=>[2,3,6](처음 칠하는 곳)
# result 2
# 2023-06-02 start 10:05 - 10:43
# 채점 : 34.0/100.0

def solution(n, m, section):
    answer = 0

    # # [false, false, false, false, false, false, false, false]
    status = [False for i in range(n)]
    # # [false, true, true, false, false, true, false, false]
    for ch in section:
        status[ch-1] = True
    # print(status)

    # true 가 있는 영역에 페인트 다시 칠하기
    for idx, st in enumerate(status):
        if(st == True):
            for i in range(m-1):
                status[i+1] = False
            answer = answer+1

    print(answer)
    return answer

if __name__ == '__main__':
    solution(8, 4, [2, 3, 6])