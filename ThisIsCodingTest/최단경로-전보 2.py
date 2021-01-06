import sys
import heapq

sys.stdin = open("최단경로-전보.txt", "r")
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        X, Y, Z = map(int, input().split())
        graph[X].append((Y,Z))

    INF = int(10e9)
    distancec = [INF] * (N+1)
    HQ = []
    heapq.heappush(HQ,(C,0))
    distancec[C] = 0
    while HQ:
        now, dist = heapq.heappop(HQ)
        for nxt, nxtd in graph[now]:
            if nxtd + distancec[now] < distancec[nxt]:
                heapq.heappush(HQ,(nxt,nxtd + distancec[now]))
                distancec[nxt] = nxtd + distancec[now]
    print(distancec)
    temp = [e for e in distancec[1:] if e != INF and e != 0]
    print(len(temp), max(temp))