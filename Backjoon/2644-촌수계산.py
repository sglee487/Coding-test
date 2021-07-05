from collections import deque
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("2644-촌수계산-2.txt", "r")

input = sys.stdin.readline

n = int(input())
ta, tb = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = -1
Q = deque()
visited = [False] * (n+1)
Q.append((ta,0))
visited[ta] = True
while Q:
    now, ch = Q.popleft()
    for child in graph[now]:
        if not visited[child]:
            visited[child] = True
            if child == tb:
                answer = ch+1
                break
            Q.append((child, ch+1))

print(answer)