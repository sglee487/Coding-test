import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    lines = []
    for _ in range(N):
        lines.append(tuple(map(int, input().split())))

    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if lines[i][0] < lines[j][0] and lines[i][1] > lines[j][1]:
                count += 1
            if lines[i][0] > lines[j][0] and lines[i][1] < lines[j][1]:
                count += 1

    print("#{}".format(test_case), count)
    # ///////////////////////////////////////////////////////////////////////////////////
