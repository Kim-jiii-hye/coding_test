# 명예의 전당(1)

# 2023-06-17 start 21:31 - stop 23:10 not solved
# 2023-06-18 start 18:30 - stop 19:18 testcase solved
# 2023-06-18 start 19:30 - stop 20:00 solved

# 채점 : 100.0/100.0

def solution(k, score):
    answer = []
    k_list = []
    for i in score:
        print(i)
        k_list.append(i)
        if len(k_list) > k:
            list_min = k_list.index(min(k_list))
            del k_list[list_min]
        k_list.sort(reverse=True)
        print(k_list)
        answer.append(min(k_list))
    print(answer)
    return answer


if __name__ == '__main__':
    solution(3, [10, 100, 20, 150, 1, 100, 200])
    # solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])
