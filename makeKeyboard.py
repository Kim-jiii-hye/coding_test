# keymap ["ABACD", "BCEFD"]
# targets ["ABCD","AABB"]
# result [9, 4]
# 2023-06-03 start 07:30 - stop 07:36
# 채점 : 52.0 / 100.0

def solution(keymap, targets):
    # 1번 키에 A, B, C 순서대로 문자 할당 => 한번 누르면 A 두번 누르면 B 세번 누르면 C
    answer = []
    for tar in targets:
        res = 0
        for target in tar:
            conc = []
            for key in keymap:
                for (idx, i) in enumerate(key):
                    if(i == target):
                        # print(f'i:{i}, idx:{idx}')
                        conc.append(idx)
                        break
                    else:
                        continue
            if(len(conc) > 0):
                res = res + (min(conc) + 1)
            else:
                res = res - 1
        answer.append(res)
    print(answer)
    return answer

if __name__ == '__main__':
    solution(["ABACD", "BCEFD"],["ABCD","AABB"])
    solution(["AA"],["B"])
    solution(["AGZ", "BSSS"], ["ASA","BGZ"])




