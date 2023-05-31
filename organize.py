# 바탕화면 정리
# wallpaper -> ["..........", ".....#....", "......##..", "...##.....", "....#....."]
# result [1, 3, 5, 8]
# 2023-06-01 start 07:10 - stop 08:20
# 채점 : 100.0/100.0

def solution(wallpaper):
    answer = []

    # wallpaper tuple로 변환 [(1, 5), (2, 6), (2, 7), (3, 3), (3, 4), (4, 4)]
    result = []
    for idx, i in enumerate(wallpaper):
        data = list(i)
        for jdx, j in enumerate(data):
            if j != '#':
                continue
            result.append((idx, jdx))
    # answer.append(0)
    # 의 최초 (0, c) => 배열 시작 1
    # answer.append(min(result[0]))
    # x축의 최소 (1, a) y축의 최대 (b, 7)
    # (lux, luy) , (rdx, rdy)
    # y축의 최소 (1, 3) x축의 최대 (4, 7)

    p1 = []
    p2 = []
    for i in result:
        p1.append(i[0])
        p2.append(i[1])

    #
    lux = min(p1)
    luy = min(p2)
    rdx = max(p1)
    rdy = max(p2)
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx + 1)
    answer.append(rdy + 1)
    print(answer)
    return answer

if __name__ == '__main__':
    solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])