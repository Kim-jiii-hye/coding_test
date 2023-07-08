# 성격 유형 검사하기
#
# 2023-07-08 09:30 - 11:01
# 채점 : 20.0/100.0

def solution(survey, choices):
    answer = ''
    result = []

    for (idx, i) in enumerate(choices):
        res = ''
        if i > 4:
            # print(f"동의:{i} - {survey[idx][1]}형 {(i + 3) - 7}점")
            res = res + survey[idx][1] + str((i + 3) - 7)
        elif i < 4:
            # print(f"비동의:{i} - {survey[idx][0]}형 {7 - (i+3)}점")
            res = res + survey[idx][0] + str(7 - (i+3))
        elif i == 4:
            # print(f"no {i}")
            res = res + survey[idx][1] + str(0)
        result.append(res)
    # print(result)
    data = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    for r in result:
        for (dx, d) in enumerate(data):
            if r[0] in d:
                # print(f"r:{r} d:{d} dx:{dx}")
                # print(data[dx])
                get_d = [i for i in range(len(data[dx])) if r[0] in data[dx][i]][0]
                data[dx][get_d] = r
    print(data)
    for (dx, d) in enumerate(data):
        print(d)
        if len(d[0]) == len(d[1]):
            answer = answer + d[0][0]
        elif len(d[0]) > len(d[1]):
            answer = answer + d[0][0]
        elif len(d[0]) < len(d[1]):
            answer = answer + d[1][0]

        # for (djx, dj) in enumerate(d):
        #     print(f"d:{dx} dj:{dj}")
        #     if len(dj) > 1: # 1보다 크면 숫자가 있는 거임
        #         answer = answer + dj[0]
        #     elif

    print(answer)
    return answer


if __name__ == '__main__':
    solution(["AN", "CF", "MJ", "RT", "NA"]	, [5, 3, 2, 7, 5])
    solution(["TR", "RT", "TR"], [7, 1, 3])


