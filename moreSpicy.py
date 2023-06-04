# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# scoville [1, 2, 3, 9, 10, 12]
# K 7
# [1+(2*2)=5, 3, 9, 10, 12]
# [3+(5*2)=13, 9, 10, 12]
# return 2
# 2023-06-04 start 11:20 - stop 11:58
# 채점 : 29.0 / 100.0

def solution(scoville, K):
    answer = 0
    for i in scoville:
        if i <= K:
            scoville.sort()
            first = min(scoville)
            first_idx = scoville.index(first)
            scoville.pop(first_idx)
            second = min(scoville)
            second_idx = scoville.index(second)
            scoville.pop(second_idx)

            mix = first + (second * 2)

            scoville.insert(first_idx, mix)
            answer = answer + 1
    return answer

if __name__ == '__main__':
    solution([1, 2, 3, 9, 10, 12], 7)




