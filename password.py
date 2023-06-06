# 둘만의 암호
# s "aukks"
# skip "wbqd"
# index 5
# result "happy"
# 2023-06-07
# 채점 : 18.0/100.0

from string import ascii_lowercase

def solution(s, skip, index):
    alph = list(ascii_lowercase)
    s_list = list(s)
    k_list = list(skip)
    print(len(alph))
    print(s_list)
    print(k_list)
    answer = ''
    for i in s_list:
        alph_idx = alph.index(i)
        target_idx = alph_idx+index
        pas = 0
        for j in range(target_idx+1):
            if alph[j] in skip:
                pas = pas

        id = target_idx+pas
        print(id)
        if id < len(alph):
            print(alph[id])


    return answer

if __name__ == '__main__':
    solution("aukks", "wbqd", 5)
