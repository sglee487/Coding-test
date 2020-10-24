import heapq
import sys

sys.stdin = open("최단경로-전보.txt", "r")
input = sys.stdin.readline

def dijkstra(start):
    Q = []
    distance = [1001] * (N+1)
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
    N, M, C = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        X, Y, Z = map(int, input().split())
        graph[X].append((Y,Z))
    distance = dijkstra(C)
    td = [i for i in distance if (i != 0 and i != 1001)]
    print(len(td), max(td))