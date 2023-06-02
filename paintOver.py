# 덧칠하기
# n=>4(총 칸 개수) m=>1(롤러의 길이) section=>[1,2,3,4](처음 칠하는 곳)
# result 4
# 2023-06-02 start 10:48 - 11:30
# 채점 : 18.0/100.0

def solution(n, m, section):
    answer = 0
    # status = []
    # 2, 3, 4, 5
    # 3, 4, 5, 6
    # 만약 최대 값이 section 의 최대값과 같다면 그만
    if(len(section) <= n):
        for i in section:
            if ((i-1) + m <= n):
                answer = answer + 1
            # else:


            # print(status)
        print(answer)

    return answer

if __name__ == '__main__':
    solution(8, 4, [2, 3, 6])
    solution(4, 1, [1, 2, 3, 4])