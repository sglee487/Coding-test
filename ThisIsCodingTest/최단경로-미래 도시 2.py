import sys

sys.stdin = open("최단경로-미래 도시.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    INF = int(10e9)
    graph = [[INF] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        print(test_case,N,a,b)
        graph[a][b] = 1
        graph[b][a] = 1
    X, K = map(int, input().split())

    for i in range(1, N+1):
        graph[i][i] = 0
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
    print(*graph,sep='\n')
    if graph[1][K] + graph[K][X] >= INF:
        print(-1)
    else:
        print(graph[1][K] + graph[K][X])