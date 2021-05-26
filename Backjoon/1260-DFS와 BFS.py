import sys
sys.setrecursionlimit(10**9)
from collections import deque


sys.stdin = open("1260-DFS와 BFS-1.txt", "r")

# input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

visited = [0] * (N+1)
visited[V] = 1
results_dfs = [V]
def dfs(now):
    for child in graph[now]:
        if not visited[child]:
            visited[child] = 1
            results_dfs.append(child)
            dfs(child)

dfs(V)
print(*results_dfs)

visited = [0] * (N+1)
visited[V] = 1
results_bfs = [V]
def bfs(start):
    Q = deque()
    Q.append(start)
    while Q:
        now = Q.popleft()
        for child in graph[now]:
            if not visited[child]:
                visited[child] = 1
                results_bfs.append(child)
                Q.append(child)

bfs(V)
print(*results_bfs)