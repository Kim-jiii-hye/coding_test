# name ["may", "kein", "kein","radi"]
# yearning [5,10,1,3]
# photo [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
# result [19, 15, 6]
# 2023-05-30 start 07:10 - stop 07:36
# 채점 : 100.0/100.0

def solution(name, yearning, photo):
    answer = []
    get_score = dict(zip(name, yearning))
    for idx, i in enumerate(photo):
        data = 0
        for j in i:
            if(j in name):
                data += get_score[j]
        answer.append(data)

    return answer

if __name__ == '__main__':
    solution(['may', 'kein', 'kain','radi'], [5,10,1,3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])


