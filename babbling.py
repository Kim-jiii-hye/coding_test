# 옹알이(2)
#

# 2023-06-26 start 07:14 -

# 채점 : 0.0/100.0
def solution(babbling):
    answer = 0
    babb = ["aya", "ye", "woo", "ma"]

    for (idx, i) in enumerate(babbling):
        res = ''
        for j in babb:
            # print(f"idx:{idx} i:{i} j:{j}")
            if j in i:
                res = res + j
        print(f"True:{res}")




if __name__ == '__main__':
    solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
