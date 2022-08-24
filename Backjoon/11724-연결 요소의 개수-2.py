import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("11724-연결 요소의 개수-2.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(now, group):
    global N
    for child in graph[now]:
        if groups[child] == 0:
            groups[child] = group
            dfs(child, group)


groups = [0] * (N+1)
group = 1

for i in range(1,N+1):
    if groups[i] != 0: continue
    groups[i] = group
    dfs(i, group)
    group += 1

print(max(groups))