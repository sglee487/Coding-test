import sys
import heapq

sys.stdin = open("최단경로-개선된 다익스트라 알고리즘.txt",'r')
input = sys.stdin.readline
INF = int(10e9)

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0
    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist: continue
        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(hq,(cost,b))

dijkstra(start)

for i in range(1, N+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])