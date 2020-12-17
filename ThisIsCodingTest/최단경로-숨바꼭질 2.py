import sys
import heapq

sys.stdin = open("최단경로-숨바꼭질.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    distances = [10e9] * (N+1)
    distances[1] = 0
    hq = []
    heapq.heappush(hq,(0,1))
    while hq:
        dist, now = heapq.heappop(hq)
        if distances[now] < dist: continue
        for n in graph[now]:
            cost = dist + 1
            if cost < distances[n]:
                distances[n] = cost
                heapq.heappush(hq,(cost,n))
    # print(distances)
    room = distances.index(max(distances[1:]))
    print(room,distances[room],distances.count(distances[room]))