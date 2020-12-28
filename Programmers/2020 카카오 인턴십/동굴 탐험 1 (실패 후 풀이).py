# https://programmers.co.kr/learn/courses/30/lessons/67260?language=python3
import sys

sys.setrecursionlimit(10 ** 9)


# https://medium.com/@haeseok/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8F%99%EA%B5%B4-%ED%83%90%ED%97%98-a669d62f304d

def dfs(now):
    if visited[now]:
        return
    if not visited[prev_visited[now]]:
        next_visit[prev_visited[now]] = now
        return

    visited[now] = True

    if next_visit[now]:
        dfs(next_visit[now])

    for nxt in graph[now]:
        dfs(nxt)


def solution(n, path, order):
    global visited, prev_visited, next_visit, graph
    graph = [[] for _ in range(n)]
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n
    prev_visited = [0] * n
    next_visit = [0] * n
    for a, b in order:
        prev_visited[b] = a

    if prev_visited[0] != 0:
        return False

    visited[0] = True
    for nxt in graph[0]:
        dfs(nxt)

    return visited.count(True) == n