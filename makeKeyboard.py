# keymap ["ABACD", "BCEFD"]
# targets ["ABCD","AABB"]
# result [9, 4]
# 2023-06-03 start 07:30 - stop 07:36
# 2023-06-04 start 12:06 - stop
# 채점1 : 52.0 / 100.0
# 채점2 : 100.0 / 100.0

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
            if(len(conc) > 0 or tar in conc):
                res = res + (min(conc) + 1)
            else:
                res = -1
                break
        answer.append(res)
    print(answer)
    return answer

if __name__ == '__main__':
    solution(["ABACD", "BCEFD"],["ABCD","AABB"]) # [9, 4]
    solution(["AA"],["B"]) # [-1]
    solution(["AGZ", "BSSS"], ["ASA","BGZ"]) # [4, 6]
    solution(["ABCDE","ABBCE"], ["ABBEF"]) # [-1]
    solution(["ABCDEFGHIJK"], ["J"]) # [10]
    solution(["FFF", "FFF"], ["CCC", "CCC"]) # [-1,-1]
    solution(["AGZ", "BSSS"], ["AGY", "BSSS"]) # [-1, 7]
    solution(["A"], ["A","B"]) # [1,-1]
    solution(["AA"], ["BA"]) # [-1]
    solution(["BCE"], ["ABC"])# [-1]
    solution(["BCC"], ["ABC"])# [-1]
    solution(["ABACD", "BCEFD"], ["XABCD", "AABB"]) # [-1, 4]




