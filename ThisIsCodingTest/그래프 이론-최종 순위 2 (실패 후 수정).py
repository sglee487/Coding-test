import sys
from collections import deque

sys.stdin = open("그래프 이론-최종 순위 1.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에
TC = int(input())

for tc in range(TC):
    n = int(input())
    tl = list(map(int, input().split()))
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for ind in range(n):
        indegree[tl[ind]] = ind
    for i in range(n):
        for j in range(i+1,n):
            graph[tl[i]].append(tl[j])

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if tl.index(a) < tl.index(b):
            indegree[a] += 1
            indegree[b] -= 1
            graph[a].remove(b)
            graph[b].append(a)
        else:
            indegree[b] += 1
            indegree[a] -= 1
            graph[b].remove(a)
            graph[a].append(b)

    # print(indegree)
    # print(graph)

    Q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0: Q.append(i)
    var = False
    result = []
    count = 0
    while Q:
        if len(Q) > 1:
            var = True
            break
        now = Q.pop()
        result.append(now)
        count += 1
        for nex in graph[now]:
            indegree[nex] -= 1
            if indegree[nex] == 0:
                Q.append(nex)
    # print(var,count,result)
    if var:
        print("?")
    elif count != n:
        print("IMPOSSIBLE")
    else:
        print(*result)