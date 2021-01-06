import sys

sys.stdin = open("최단경로-간단한 다익스트라 알고리즘.txt",'r')
input = sys.stdin.readline
INF = int(10e9)

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for b,c in graph[start]:
        distance[b] = c
    for _ in range(N-1):
        now = get_smallest_node()
        visited[now] = True
        for b, c in graph[now]:
            cost = distance[now] + c
            if cost < distance[b]:
                distance[b] = cost

dijkstra(start)

for i in range(1, N+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])