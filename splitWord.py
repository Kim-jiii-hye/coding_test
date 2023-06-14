# 문자열 나누기
# t "banana"
# result 3
# 2023-06-14 start 07:10 - stop 07:40 start 22:33 - stop 07:40
# 채점 : /100.0

def solution(s):
    answer = 0
    count = {}
    for (idx,i) in enumerate(s):
        if i in count:
            count[i] = count[i] + 1
        else:
            # 다른 글자 등장
            count[i] = 1

        print(count)
        if len(count) > 1:
            # print(f"현재 문자열:{i} / 이전 문자열:{s[idx-1]}")
            data = [k for k, v in count.items() if v == count[i]]
            if len(data) > 1:
                print(s[:idx-1])
                answer = answer + 1





if __name__ == '__main__':
    solution("banana")
    solution("aaabbaccccabba")