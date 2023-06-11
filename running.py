# 1등~3등까지 선수들 달리고 있음 ["mumu","soe", "poe"]
# soe 선수 부르면 -> ["soe","mumu","poe"]
# players ["mumu", "soe","poe","kai", "mine"]
# callings ["kai","kai", "mine", "mine"]
# result ["mumu", "kai", "mine", "soe", "poe"]
# 2023-05-29 start 11:10 - stop 11:50
# 2023-06-10 start 09:35 - stop 11:40
# 채점 : 68.8/100.0 => 시간초과 실패 5개
# player는 최대 5만명까지 있을 수 있음,
# index() 선형 시간 복잡도. O(1)
# 순환문이 인덱스를 기록하면서 반복할 수 있도록 바꾸어 보기
import time

def solution(players, callings):
    report_dict = {i : string for string,i in enumerate(players)}

    for (idx, i) in enumerate(callings):
        cur_idx = report_dict[i]
        report_dict[i] = report_dict[i] - 1
        report_dict[players[cur_idx-1]] += 1
        players[cur_idx-1], players[cur_idx] = players[cur_idx], players[cur_idx-1]

        # players = sorted(report_dict, key=lambda x: report_dict[x])
        # name_b = players[report_dict[callings[idx]] - 1]
        # print(name_b)
        # # print(report_dict[name_b])
        # report_dict[name_b] = report_dict[callings[idx]]
        # report_dict[callings[idx]] = report_dict[callings[idx]] - 1
    # players = sorted(report_dict, key=lambda x: report_dict[x])


    # for calling in callings:
    #     name_b = players[report_dict[calling] - 1]
    #     print(name_b)
    #     report_dict[calling] = report_dict[calling] - 1
    #     report_dict[name_b] = report_dict[name_b] + 1
    #     # print(report_dict)

    print(players)




    # print(players)

if __name__ == '__main__':
    solution(["mumu", "soe","poe","kai", "mine"], ["kai","kai", "mine", "mine"])