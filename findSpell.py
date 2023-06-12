# 가장 가까운 같은 글자
# s "banana"
# result [-1, -1, -1, 2, 2, 2]
# 2023-06-13 start 07:03 - stop 08:38
# 채점 : 100.0/ 100.0

def solution(s):
    answer = []
    result = ''
    res = []

    for i in s:
        result = result+i
        if i not in res:
            res.append(i)
            answer.append(-1)
        else:
            # print(s[s.find(i)])
            # print(result[::-1])
            idx = []
            for (jdx, j) in enumerate(result[::-1]):

                if j == s[s.find(i)]:
                    # print(jdx)
                    idx.append(jdx)
            # print(idx)

            answer.append(idx[1] - idx[0])



    print(answer)
        # for r in result[::-1]:
        #     print(r)





    # return answer

if __name__ == '__main__':
    solution("banana")
    solution("foobar")





