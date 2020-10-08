from collections import deque
from collections import defaultdict

def solution(n, edges):
    dil = [[] for _ in range(n+1)]
    dillistdict = [defaultdict(list) for _ in range(n+1)]
    for a, b in edges:
        dil[a].append(b)
        dil[b].append(a)
        dillistdict[a][b] = 1
        dillistdict[b][a] = 1
    def distance(a, b):
        if b in dillistdict[a]:
            return dillistdict[a][b]
        Q = deque()
        visited = deque()
        Q.append((a,0))
        while Q:
            n, d = Q.popleft()
            dillistdict[a][n] = d
            dillistdict[n][a] = d
            if b in dillistdict[n]:
                dillistdict[a][b] = d + dillistdict[n][b]
                dillistdict[b][a] = d + dillistdict[n][b]
                return dillistdict[b][a]
            if n == b: return d
            visited.append(n)
            for ne in dil[n]:
                if ne not in visited:
                    Q.append((ne,d+1))
    cond = []
    cl = 1
    while len(cond) < 3:
        for i, n in enumerate(dil):
            if len(n) == cl:
                cond.append(i)
        cl += 1
    result = 0
    for i in range(len(cond)-2):
        for j in range(i+1,len(cond)-1):
            for k in range(j+1,len(cond)):
                dist = (distance(cond[i],cond[j]) + distance(cond[j],cond[k]) + distance(cond[k],cond[i])) // 3
                if dist > result:
                    result = dist
    return result

print(solution(4,[[1,2],[2,3],[3,4]]),2)
print(solution(5,[[1,5],[2,5],[3,5],[4,5]]),2)