# 명예의 전당(1)

# 2023-06-17 start 21:31 - stop 23:10 not solved
# 2023-06-18 start 18:30 - stop
# 채점 : /100.0

def solution(k, score):
    answer = []
    k_list = []
    for (idx, i) in enumerate(score):
        if len(k_list) < 1 or min(k_list) < i:
            k_list.append(i)
        if len(k_list) > k:
            # print(f"{min(k_list)} - {k_list.index(min(k_list))}빼기")
            k_list.pop(k_list.index(min(k_list)))
            # print(k_list)

        k_list.sort(reverse=True)
        print(k_list)
        answer.append(min(k_list))


    print(answer)



if __name__ == '__main__':
    # solution(3, [10, 100, 20, 150, 1, 100, 200])
    solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])
