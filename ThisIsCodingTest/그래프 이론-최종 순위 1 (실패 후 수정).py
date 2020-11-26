from collections import deque
import sys

sys.stdin = open("그래프 이론-최종 순위 1.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에
testcase = int(input())

for testcasenum in range(testcase):
    N = int(input())
    T = list(map(int, input().split()))

    Q = deque()
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    for i in range(len(T)):
        for j in range(i+1,len(T)):
            graph[T[i]].append(T[j])
            indegree[T[j]] += 1

    # print(graph)
    # print(indegree)

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        if T.index(a) < T.index(b):
            indegree[a] += 1
            indegree[b] -= 1
            graph[a].remove(b)
            graph[b].append(a)
        else:
            indegree[a] -= 1
            indegree[b] += 1
            graph[b].remove(a)
            graph[a].append(b)

    # print(graph)
    # print(indegree)

    for i in range(1,len(indegree)):
        if indegree[i] == 0:
            Q.append(i)
            
    result = []
    question = False
    while Q:
        if len(Q) != 1:
            question = True
            break
        now = Q.popleft()
        # print(Q)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                Q.append(i)

    if question:
        print("?")
    elif len(result) != len(T):
        print("IMPOSSIBLE")
    else:
        print(*result)