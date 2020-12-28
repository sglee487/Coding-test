# https://programmers.co.kr/learn/courses/30/lessons/67260?language=python3
from collections import defaultdict
from collections import deque
import sys
sys.setrecursionlimit(10**9)

def solution(n, path, order):
    graph = [[] for _ in range(n)]
    lines = [0] * n
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
        lines[a] += 1
        lines[b] += 1
    indegree = [True] * n
    indegreedict = defaultdict(int)
    for a, b in order:
        indegreedict[a] = b
        indegree[indegreedict[a]] = False
    Q = deque()
    Q.append(0)
    # print(graph)
    # print(indegree)
    # print(lines)
    visited = [False] * n
    visited[0] = True
    lines[0] -= 1
    while Q:
        now = Q.popleft()
        indegree[indegreedict[now]] = True
        for nxt in graph[now]:
            if lines[nxt] and indegree[nxt]:
                indegree[indegreedict[nxt]] = True
                visited[nxt] = True
                lines[nxt] -= 1
                Q.append(nxt)
        # print(Q)
    # print(lines)
    # print(visited)
    return visited.count(True) == n