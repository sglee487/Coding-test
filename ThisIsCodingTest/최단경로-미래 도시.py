import sys
import heapq

sys.stdin = open("최단경로-미래 도시.txt", "r")

def dijkstra(start):
    Q = []
    distance = [987654321] * (N+1)
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
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append((b,1))
        graph[b].append((a,1))
    X, K = map(int, input().split())
    dis1 = dijkstra(1)
    disk = dijkstra(K)
    print(dis1[K] + disk[X] if (dis1[K] + disk[X]) < 987654321 else -1)