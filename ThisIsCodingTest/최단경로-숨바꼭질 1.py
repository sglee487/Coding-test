import sys
from collections import deque

sys.stdin = open("최단경로-숨바꼭질.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    Q = deque()
    Q.append((1,0))
    distances = [0] * (N+1)
    visited = [False] * (N+1)
    while Q:
        room, dist = Q.popleft()
        if visited[room]: continue
        distances[room] = dist
        visited[room] = True
        for e in graph[room]:
            Q.append((e, dist+1))
        # print(distances,Q)
    ri = distances.index(max(distances))
    rd = distances[ri]
    rc = distances.count(rd)
    print(ri,rd,rc)