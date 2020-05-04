import sys

sys.stdin = open("sample_input.txt", "r")

import itertools
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())

    route = [list(map(int, input().split())) for _ in range(N)]

    cb = list(itertools.permutations(range(2,N+1),r=N-1))

    distance = []
    for tup in cb:
        sub_distance = 0
        sub_distance += route[0][tup[0]-1]
        for i in range(len(tup)-1):
            sub_distance += route[tup[i] - 1][tup[i+1] - 1]
        sub_distance += route[tup[len(tup)-1]-1][0]
        distance.append(sub_distance)

    print("#{}".format(test_case),min(distance))

    # ///////////////////////////////////////////////////////////////////////////////////
