# 숫자 문자열과 영단어

# 2023-07-12 start 08:33 -
# 2023-07-13 start 07:10 - 07:37

# 채점 : 100.0/100.0
def solution(s):
    data = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    check = ''
    answer = s
    for (idx, i) in enumerate(s):
        if not i.isdigit():
            if check not in data:
                check = check + i
            if check in data:
                # print(check)
                # print(data.index(check))
                answer = answer.replace(check, str(data.index(check)))
                check = ''
    print(answer)
    return int(answer)




        # if check in data:
        #     print(idx)
        #     print(check)
        #     check = ''


if __name__ == '__main__':
    solution("one4seveneight")
