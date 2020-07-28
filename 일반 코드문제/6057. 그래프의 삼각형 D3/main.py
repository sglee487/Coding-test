import sys
from collections import deque

sys.stdin = open("s_input.txt", "r")

def go():
    global tri_count

    Q = deque()
    for n in range(1,N+1):
        Q.append((n,ways[n],1))
    while Q:
        si, way, rank = Q.pop()
        for w in range(1, N+1):



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    ways = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        ways[a][b], ways[b][a] = 1, 1

    tri_count = 0
    print(ways)

    go()


    print("#{}".format(test_case))
    # ///////////////////////////////////////////////////////////////////////////////////
