# 숫자 문자열과 영단어

# 2023-07-12 start 08:33 -

# 채점 : 0/100.0
def solution(s):
    check = ''
    data = ['zero', 'one', 'two', 'three','four', 'five', 'six', 'seven', 'eight', 'nine']
    for (idx, i) in enumerate(s):
        print(i)
        if check not in data:
            check = check + i
        else:

            print(f"check:{check} idx:{idx}")


if __name__ == '__main__':
    solution("one4seveneight")
