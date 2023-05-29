# 1등~3등까지 선수들 달리고 있음 ["mumu","soe", "poe"]
# soe 선수 부르면 -> ["soe","mumu","poe"]
# players ["mumu", "soe","poe","kai", "mine"]
# callings ["kai","kai", "mine", "mine"]
# result ["mumu", "kai", "mine", "soe", "poe"]
# 2023-05-29 start 11:10 - stop 11:50
# 채점 : 68.8/100.0 => 시간초과 실패 5개

def solution(players, callings):
    answer = []
    for calling in callings:
        call = players.index(calling)
        temp = players[call - 1]
        players[call - 1] = calling
        players[call] = temp
        answer = players
    print(answer)
    return answer

if __name__ == '__main__':
    solution(["mumu", "soe","poe","kai", "mine"], ["kai","kai", "mine", "mine"])