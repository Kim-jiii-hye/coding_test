# 옹알이(2)

# 2023-06-26 start 07:14 - 07:30 not solved
# 2023-06-27 start 21:12 - 22:33 not solved
# 2023-06-28 start -

# 채점 : 45.0/100.0
def solution(babbling):
    answer = 0
    babb = ["aya", "ye", "woo", "ma"]

    for (idx, i) in enumerate(babbling):
        result = ''
        res = []
        for spell in i:
            if result not in babb:
                result = result + spell
                res.append(result)
            if result in babb:
                # print(f"result:{result} index: {babb.index(result)}")
                res.append(babb.index(result))
                result = ''
        print(f"res:{res}")
        cnt = 0
        for (jdx,j) in enumerate(res):
            if type(j) == int:
                cnt = cnt + 1
                # print(f"cnt:{cnt} jdx:{jdx}")
                if cnt == 1:
                    res = res[jdx:]
                    print(f"cnt:1 {res}")
                else:
                    test = jdx - cnt
                    # print(test)
                    print(f"cnt:{cnt}    jdx:{jdx} res:{res} len:{len(res)} test:{test}")





                # res = res[jdx:]
        #         # print(res[jdx:])
        # print(f"res:{res}")
        # for (jdx, j) in enumerate(res):

        #
        # for (jdx, j) in enumerate(res):
        #     if jdx+1 < len(res):
        #         # print(f"{jdx}일 때 {jdx+1}")
        #         if res[jdx] != res[jdx+1]:
        #             answer = answer + 1
        #             break
    print(f"answer : {answer}")


if __name__ == '__main__':
    solution(["aya", "yee", "u", "maa"])
    solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
