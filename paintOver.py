# 덧칠하기
# n=>4(총 칸 개수) m=>1(롤러의 길이) section=>[1,2,3,4](처음 칠하는 곳)
# result 4
# 2023-06-02
# 채점 : 18.0/100.0

def solution(n, m, section):
    # 정답 참고.. .
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    #
    # if (1 <= m and m<=n and n<=100000):
    #     if(1 <= len(section) <= n):
    #         for i in section:
    #             if ((i-1) + m <= n):
    #                 answer = answer + 1
    #         print(answer)
    print(answer)
    return answer

if __name__ == '__main__':
    solution(8, 4, [2, 3, 6])
    solution(5, 4, [1,3])
    solution(4, 1, [1, 2, 3, 4])