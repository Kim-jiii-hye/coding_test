# 숫자 문자열과 영단어

# 2023-07-12 start 08:33 -

# 채점 : 0/100.0
def solution(s):

    data = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    print(s)
    check = ''
    for (idx, i) in enumerate(s):
        if check.isdigit() == False:
            check = check + i
            print(check)

        if check in data:
            print(idx)
            print(check)
            check = ''


if __name__ == '__main__':
    solution("one4seveneight")
