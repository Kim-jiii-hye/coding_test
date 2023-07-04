# 숫자 짝꿍
#
#
# 2023-07-04 21:40 - 22:28
# 채점 : 36.8/100.0
from itertools import *
def solution(X, Y):
    res = []
    list_X = list(X)
    list_Y = list(Y)

    for i in list_X:
        for (jdx, j) in enumerate(list_Y):
            if i == j:
                res.append(i)
                list_Y.pop(jdx)
    # print(res)
    res_list = list(permutations(res,len(res)))
    # print(res_list)
    result_arr = []
    for r in res_list:
        data = ''.join(r)
        if data not in result_arr:
            result_arr.append(''.join(r))

    if '' not in result_arr:
        result_list = list(map(int, result_arr))
        # print(result_list)
        answer = max(result_list)
    else:
        answer = -1
    print(str(answer))




if __name__ == '__main__':
    solution("100", "2345")
    solution("100", "203045")
    solution("100", "123450")
    solution("12321", "42531")
    solution("5525", "1255")


