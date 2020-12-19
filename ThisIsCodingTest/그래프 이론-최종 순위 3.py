import sys
from collections import deque

sys.stdin = open("그래프 이론-최종 순위 1.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에
TC = int(input())

for tc in range(TC):
    N = int(input())
    til = list(map(int, input().split()))

    graph = [[] for _ in range(N+1)]
    for i in range(N):
        for j in range(i,N):
            graph[til[i]].append(til[j])

    indegree = [0] * (N+1)
    for i, e in enumerate(til):
        indegree[e] = i

    # print(graph)
    # print(indegree)

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        if til.index(a) < til.index(b):
            graph[a].remove(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[b] += 1
            indegree[a] -= 1

    Q = deque()
    for i, e in enumerate(indegree[1:],1):
        if e == 0:
            Q.append(i)
    cut = False
    result = []
    while Q:
        if len(Q) > 1:
            cut = True
            break
        now = Q.popleft()
        result.append(now)
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                Q.append(nxt)
    if cut:
        print("?")
    elif len(result) < N:
        print("IMPOSSIBLE")
    else:
        print(*result)