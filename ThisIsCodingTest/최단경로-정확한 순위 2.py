import sys
from collections import deque

sys.stdin = open("최단경로-정확한 순위.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    winvsgraph = [[] for _ in range(N+1)]
    losevsgraph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        winvsgraph[a].append(b)
        losevsgraph[b].append(a)
    result = 0
    for n in range(1,N+1):
        wc = 0
        visited = [False] * (N+1)
        visited[n] = True
        Q = deque(winvsgraph[n])
        while Q:
            nn = Q.popleft()
            if visited[nn]: continue
            wc += 1
            visited[nn] = True
            for w in winvsgraph[nn]:
                if not visited[w]: Q.append(w)

        lc = 0
        visited = [False] * (N + 1)
        visited[n] = True
        Q = deque(losevsgraph[n])
        while Q:
            nn = Q.popleft()
            if visited[nn]: continue
            lc += 1
            visited[nn] = True
            for w in losevsgraph[nn]:
                if not visited[w]: Q.append(w)

        if wc + lc == N-1: result += 1
    print(result)