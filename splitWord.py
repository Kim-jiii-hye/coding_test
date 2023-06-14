# 문자열 나누기
# t "banana"
# result 3
# 2023-06-14 start 07:10 - stop 07:40 start 22:33 - stop 07:40
# 2023-06-15 start 07:07 - stop 07:42
# 채점 : 28.6/100.0

def solution(s):
    answer = 0
    status = False
    count = {}
    for (idx,i) in enumerate(s):
        if i in count:
            count[i] = count[i] + 1
        else:
            # 다른 글자 등장
            print(f"다른 글자 등장{i}")
            status = True
            count[i] = 1
        print(count)
        if(status):
            print(f"현재{i}-{count[i]}찾기")
            s_li = []
            for j in count:
                if count[j] == count[i]:
                    s_li.append(count[j])
            if(len(s_li) > 1 or idx == len(s)-1):
                c = 0
                print(f"{idx+1} : {s[c:idx+1]}")
                answer = answer + 1
                count = {}

    print(answer)



if __name__ == '__main__':
    # solution("banana")
    solution("abracadabra")
    # solution("aaabbaccccabba")