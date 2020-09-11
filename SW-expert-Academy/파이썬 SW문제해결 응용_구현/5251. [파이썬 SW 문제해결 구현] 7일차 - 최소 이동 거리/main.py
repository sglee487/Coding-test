import sys

sys.stdin = open("sample_input.txt", "r")

def Dijkstra(G, r):
    D = [INF] * (N+1)
    P = [None] * (N+1)
    visited = [False] * (N+1)
    D[r] = 0

    for _ in range(N):
        minIndex = -1
        min = INF
        for i in range(N):
            if not visited[i] and D[i] < min:
                min = D[i]
                minIndex = i
        visited[minIndex] = True
        for v, val in G[minIndex]:
            if not visited[v] and D[minIndex] + val < D[v]:
                D[v] = D[minIndex] + val
                P[v] = minIndex
    return D,P

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, E = map(int, input().split())
    INF = 1000000

    G = [list() for _ in range(N)]
    for _ in range(E):
        index, v, val = map(int, input().split())
        G[index].append((v,val))

    D,P = Dijkstra(G,0)

    print("#{}".format(test_case),D[N])

    # ///////////////////////////////////////////////////////////////////////////////////
