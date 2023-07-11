# 최소 직사각형
#
# 2023-07-10
# 채점 : /100.0

def solution(sizes):
    print(sizes)
    for (idx, i) in enumerate(sizes):
        for (jdx, j) in enumerate(i):
            print(f"j:{j} jdx:{jdx}")

if __name__ == '__main__':
    # solution([[60, 50], [30, 70], [60, 30], [80, 40]])
    solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
    # solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])


