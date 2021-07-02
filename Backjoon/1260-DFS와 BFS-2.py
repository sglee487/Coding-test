import sys
sys.setrecursionlimit(10**9)
from collections import deque


sys.stdin = open("1260-DFS와 BFS-1.txt", "r")
input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,N+1):
    graph[i].sort()

def dfs(now):
    print(now, end=' ')
    for child in graph[now]:
        if not visited_dfs[child]:
            visited_dfs[child] = True
            dfs(child)
    return

def bfs(now):
    Q = deque()
    Q.append(now)
    visited_bfs = [False] * (N+1)
    visited_bfs[now] = True
    while Q:
        now = Q.popleft()
        print(now, end=' ')
        for child in graph[now]:
            if not visited_bfs[child]:
                visited_bfs[child] = True
                Q.append(child)

    return

visited_dfs = [False] * (N+1)
visited_dfs[V] = True
dfs(V)
print()
bfs(V)