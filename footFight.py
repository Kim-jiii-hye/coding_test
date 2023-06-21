# 과일 장수
# 1대1 대결. 매 대결마다 음식 종류, 양 바뀜

# 2023-06-22 start 07:04 - 07:22

# 채점 : 100.0/100.0
def solution(food):
    print(food)
    half_answer = ''
    reverse_answer = ''
    for (food_cnt, i) in enumerate(food):
        water = food[0] # 수웅이가 준비한 물의 양. 항상 1
        if food_cnt > 0:
            print(f"칼로리 적은 순 {food_cnt}번 음식 {i}개")
            for j in range(1, int(i/2)+1):
                half_answer = half_answer + str(food_cnt)

    for c in half_answer:
        reverse_answer = c + reverse_answer

    answer = half_answer + '0' + reverse_answer
    print(answer)


if __name__ == '__main__':
    solution([1, 3, 4, 6])
    solution([1, 7, 1, 2])

