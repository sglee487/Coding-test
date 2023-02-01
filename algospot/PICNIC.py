import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("PICNIC.txt", "r")

input = sys.stdin.readline


def dfs(matches, graph):
    if all(matches):
        return 1

    ret = 0
    i = matches.index(False)
    for j in graph[i]:
        if not matches[i] and not matches[j]:
            matches[i] = True
            matches[j] = True
            ret += dfs(matches, graph)
            matches[i] = False
            matches[j] = False

    return ret


C = int(input())
for _ in range(C):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    fl = list(map(int, input().split()))
    for i in range(0, len(fl), 2):
        a, b = min(fl[i], fl[i + 1]), max(fl[i], fl[i + 1])
        graph[a].append(b)
    for i in range(n):
        graph[i].sort()

    matches = [False] * n
    print(dfs(matches, graph))
