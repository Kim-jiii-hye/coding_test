# 옹알이(2)

# 2023-06-26 start 07:14 - 07:30 not solved
# 2023-06-27 start 21:12 - 22:33 not solved

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
            if result in babb:
                print(f"result:{result} index: {babb.index(result)}")
                res.append(babb.index(result))
                result = ''


        print(res)

        for (jdx, j) in enumerate(res):
            if jdx+1 < len(res):
                # print(f"{jdx}일 때 {jdx+1}")
                if res[jdx] != res[jdx+1]:
                    answer = answer + 1
                    print(f"{answer}추가")
                    break
    print(f"answer : {answer}")


if __name__ == '__main__':
    solution(["aya", "yee", "u", "maa"])
    solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
