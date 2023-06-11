# 크기가 작은 부분문자열
# t "3141592"
# p "271"
# result 2
# 2023-06-12 start 07:20 - stop 08:40
# 채점 : 100.0/100.0

def solution(t, p):
    p_spl = len(p)
    t_lst = list(t)

    res = []
    for (idx, i) in enumerate(t_lst):
        t_res = ''
        if idx <= (len(t_lst) - p_spl):
            for j in range(p_spl):
                t_res = t_res + t_lst[idx+j]
        else:
            break
        res.append(t_res)
    # print(res)
    list_a = list(map(int, res))
    # print(list_a)
    answer = 0
    for i in list_a:
        if i <= int(p):
            answer = answer + 1
    print(answer)

if __name__ == '__main__':
    solution("3141592", "271")
    solution("500220839878", "7")
    solution("10203", "15")