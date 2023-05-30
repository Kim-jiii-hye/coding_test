# park ["SOO", "OOO", "OOO"]
# routes ["E 2", "S 2", "W 1"]
# result [2,1]
# 2023-05-31 start 07:05 - pause 07:50
# 채점 :

def p(res):
    result = list(res)
    return result


def solution(park, routes):

    answer = [0, 0]

# 이동거리 1 <= n <= 9
    result = p(park)
    for idx, i in enumerate(routes):
        result = p(park[idx])
        route = i.split(' ')

        if(route[0] == 'E'):
            bef = answer[1]
            answer = [answer[0], bef+int(route[1])]
        elif(route[0] == 'S'):
            bef = answer[0]
            answer = [bef+int(route[1]), answer[1]]
        elif(route[0] == 'W'):
            bef = answer[1]
            answer = [answer[0], bef-int(route[1])]
        elif(route[0] == 'N'):
            bef = answer[0]
            answer = [bef + int(route[1]), answer[1]]
        print(result)
        # 장애물 추가
    print(answer)

    return answer

if __name__ == '__main__':
    solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"])