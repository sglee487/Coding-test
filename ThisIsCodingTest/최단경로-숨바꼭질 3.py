from collections import deque
import sys

sys.stdin = open("최단경로-숨바꼭질.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    Q = deque()
    Q.append(1)
    distances = [20001] * (N+1)
    distances[1] = 0
    while Q:
        now = Q.popleft()
        for nxt in graph[now]:
            if distances[nxt] < distances[now] + 1: continue
            distances[nxt] = distances[now]+1
            Q.append(nxt)
    print(distances)
    print(distances.index(max(distances[1:])),max(distances[1:]),distances[1:].count(max(distances[1:])))