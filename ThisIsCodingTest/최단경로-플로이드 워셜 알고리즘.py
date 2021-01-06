import sys

sys.stdin = open("최단경로-플로이드 워셜 알고리즘.txt", "r")
input = sys.stdin.readline

INF = int(10e9)
N = int(input())
M = int(input())
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과 출력
for a in range(1, N+1):
    for b in range(1, N+1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()