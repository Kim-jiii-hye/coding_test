# 리스트안에 순서는 변경할 수 없음
# cards1 ["i", "drink", "water"]
# cards2 ["want", "to"]
# goal ["i", "want", "to", "drink", "water"]
# 0 cards1 i, 1 cards2 want to
# result "Yes"
# 2023-06-06 start 14:00 - stop 15:20
# 채점 : 72.0 / 100.0 => 84.0 / 100.0

def solution(cards1, cards2, goal):

    for (idx, i) in enumerate(goal):
        if i in cards2:
            cards1.insert(idx, i)

    # print(cards1)
    # print(goal)
    if cards1 == goal:
        answer = "Yes"
    else:
        answer = "No"
        for (idx, i) in enumerate(goal):
            if (i == cards1[idx]):
                answer = "Yes"
            else:
                answer = "No"

    print(answer)
    # if cards1 == goal:
    #     answer = "Yes"
    # else:
    #     answer = "No"
    # print(cards1)
    # print(goal)
    # print(answer)

    # return answer

if __name__ == '__main__':
    solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])
    solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])
    solution(["i", "drink", "water"], ["want", "to", "juice"], ["i", "want", "to", "drink", "water"])
    solution(["i", "drink", "water"], ["want", "to", "juice"], ["i", "want", "to", "drink", "juice"])




