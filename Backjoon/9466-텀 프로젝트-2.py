import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("9466-텀 프로젝트-1.txt", "r")

input = sys.stdin.readline


def dfs(now):
    global n, graph, visited, done, paired_num
    if not visited[now]:
        visited[now] = True
        dfs(graph[now])
    elif visited[now] and not done[now]:
        nxt = graph[now]
        while nxt != now:
            done[nxt] = True
            nxt = graph[nxt]
            paired_num += 1
        paired_num += 1
    done[now] = True


T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    done = [False] * (n + 1)
    paired_num = 0
    for i in range(1, n + 1):
        dfs(i)
    print(n - paired_num)
