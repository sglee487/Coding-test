import sys
from collections import deque

sys.stdin = open("sample_input.txt", "r")

def color_tree(n):
    global result

    Q = deque()
    Q.append((1,[0] * (N + 1)))
    while Q:
        n, c = Q.popleft()
        if n == N+1:
            print("possible")
            result = 1
            return

        cn = [0] * (N+1)
        for t in range(1, N+1):
            if WM[n][t] == 0: continue
            else: cn[t] = c[t]
        for m in range(1,M+1):
            if m in cn: continue
            c[n] = m
            print(n, m, c[:])
            Q.append((n+1,c[:]))

    # if n == N+1:
    #     print("possible")
    #     result = 1
    #     return
    #
    # cn = [0] * (N+1)
    # for t in range(1, N+1):
    #     if WM[n][t] == 0: continue
    #     else: cn[t] = C[t]
    #
    # for m in range(1,M+1):
    #     if m in cn: continue
    #     C[n] = m
    #     print(n, m, C)
    #     color_tree(n+1)
    #     C[n] = 0
    # return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, E, M = map(int, input().split())
    WM = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        f, s = map(int, input().split())
        WM[f][s], WM[s][f] = 1, 1

    C = [0] * (N + 1)
    result = 0
    color_tree(1)

    print("#{}".format(test_case),result)
    # ///////////////////////////////////////////////////////////////////////////////////
