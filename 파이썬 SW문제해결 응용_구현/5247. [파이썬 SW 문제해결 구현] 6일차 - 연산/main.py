import sys

sys.stdin = open("sample_input.txt", "r")
from collections import deque
def find(S,E):
    global min_h
    Q.append((S,0))
    # calculated.append(S)
    if S == E:
        min_h = 0

    while Q:
        v = Q.popleft()
        # backtracking
        if v[1] >= min_h:
            continue
        if v[0] < 1 or v[0] > 1000000:
            continue

        if v[0] == E:
            # 너비우선적으로 찾으므로 찾았다면 바로 게임 끝
            min_h = v[1]
            return

        if calculated[v[0]] == test_case:
            continue
        calculated[v[0]] = test_case

        Q.append((v[0] + 1, v[1] + 1))
        Q.append((v[0] - 10, v[1] + 1))
        Q.append((v[0] - 1, v[1] + 1))
        Q.append((v[0] * 2, v[1] + 1))
        # print(v,Q)

    pass

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    S, E = map(int, input().split())

    # 재귀로 하기엔 경우의 수가 너무 많아서 힘들것 같은데... 너비 우선으로 큐를 써야 할듯.
    calculated = [0] * 10000001
    min_h = 1000000
    Q = deque()
    find(S,E)
    # print(min_h)

    print("#{}".format(test_case),min_h)

    # ///////////////////////////////////////////////////////////////////////////////////
