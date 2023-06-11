# park ["SOO", "OOO", "OOO"]
# routes ["E 2", "S 2", "W 1"]
# result [2,1]
# 2023-05-31 start 07:05 - stop 07:50
# 2023-06-10 start 11:50 - stop
# 채점 :

def solution(park, routes):
    x = 0
    y = 0
    for (idx, r) in enumerate(routes):
        route = r.split(' ')
        park_list = list(park[idx])
        for i in range(int(route[1])+1):
            # 0 1
            if(i < len(park_list)):
                if park_list[i] == 'S':
                    x = 0
                    y = 0
                    print("init")
                    continue
                elif park_list[i] == 'O':
                    if route[0] == 'N':
                        x = x - 1
                        print(f"N: {x} - {int(route[1])}")
                    elif route[0] == 'S':
                        x = x + 1
                        print(f"S: {x} - {int(route[1])}")
                    elif route[0] == 'W':
                        y = y - 1
                        print(f"W:{y} -  {int(route[1])}")
                    elif route[0] == 'E':
                        y = y + 1
                        print(f"E:{y} -  {int(route[1])}")
                    print("go")
                    continue
                elif park_list[i] == 'X':
                    print("stop")
                    continue
        answer = [x, y]
        print(answer)
    # for (idx,s) in enumerate(park):
    #     route = routes[idx].split(' ')
    #     for j in s:
    #         if j == 'S':
    #             print("시작지점")
    #             x = 0
    #             y = 0
    #             continue
    #         elif j == 'O':
    #             print("지나다니기")
    #             if route[0] == 'N':
    #                 x = x - int(route[1])
    #                 print(f"N: {int(route[1])}")
    #             elif route[0] == 'S':
    #                 x = x + int(route[1])
    #                 print(f"S: {int(route[1])}")
    #             elif route[0] == 'W':
    #                 y = y - int(route[1])
    #                 print(f"W: {int(route[1])}")
    #             elif route[0] == 'E':
    #                 y = y + int(route[1])
    #                 print(f"E: {int(route[1])}")

    #             continue
    #         elif j == 'X':
    #             print("장애물 있음")
    #             continue


    # 동쪽으로 두칸 [0,2]
    # 남쪽으로 두칸 [2,2]
    # 서쪽으로 한칸 [2,1]
    print(answer)
    return answer

if __name__ == '__main__':
    solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"])