# 명예의 전당(1)

# 2023-06-17 start 21:31 - stop 23:10
# 채점 : /100.0

def solution(k, score):
    answer = []
    k_list = []
    for i in score:
        if len(k_list) < k:
            k_list.append(i)
        for j in k_list:
            if i >= j:
                print(f"i:{i} j:{j} max:{max(k_list)} min:{min(k_list)}")
                if max(k_list) < i:
                    pop_idx = k_list.index(min(k_list))
                    k_list.pop(pop_idx)
                    k_list.append(i)
        k_list.sort(reverse=True)
        print(k_list)


    # print(k_list)



if __name__ == '__main__':
    solution(3, [10, 100, 20, 150, 1, 100, 200])
    # solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])