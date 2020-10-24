import sys
import heapq

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
sys.stdin = open("최단경로-플로이드.txt", "r")

def dijkstra(start):
    Q = []
    distance = [INF] * (N+1)
    distance[start] = 0
    heapq.heappush(Q,(0,start))
    while Q:
        dist, now = heapq.heappop(Q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(Q,(cost,i[0]))
    return distance


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b,c))

    for s in range(1,N+1):
        print(*[i if i != INF else 0 for i in dijkstra(s)[1:]])