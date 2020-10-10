from collections import deque

def solution(n, edge):
    ndl = [[] for _ in range(n+1)]
    for a,b in edge:
        ndl[a].append(b)
        ndl[b].append(a)
    otodl = [0] * (n+1)
    Q = deque()
    Q.append((1,0))
    visited = [False] * (n+1)
    while Q:
        n, d = Q.popleft()
        visited[n] = True
        otodl[n] = d
        for n in ndl[n]:
            if not visited[n]:
                visited[n] = True
                Q.append((n,d+1))
    return otodl.count(max(otodl))

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]),3)