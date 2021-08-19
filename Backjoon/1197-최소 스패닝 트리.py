import heapq
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("1197-최소 스패닝 트리-2.txt", "r")

input = sys.stdin.readline

V, E = map(int, input().split())
hl = []
for _ in range(E):
    a,b,c = map(int, input().split())
    heapq.heappush(hl,(c,a,b))

parents = list(range(V+1))
ranks = [0] * (V+1)

def FIND_SET(x):
    if x != parents[x]:
        parents[x] = FIND_SET(parents[x])
    return parents[x]

def LINK(x,y):
    if ranks[x] > ranks[y]:
        parents[y] = x
    else:
        parents[x] = y
    if ranks[x] == ranks[y]:
        ranks[y] += 1

def UNION(x,y):
    LINK(FIND_SET(x), FIND_SET(y))

# 파이썬 SW문제해결 응용_구현 - 07 그래프의 최소 비용 문제
print(parents)
print(ranks)
graph = [[] * (V+1) for _ in range(V+1)]
def MST_KRUSKAL(G):
    global E, V
    mst = []
    mw = 0
    while len(mst) < V-1:
        print(G)
        w, a, b = heapq.heappop(G)
        if FIND_SET(a) != FIND_SET(b):
            UNION(a,b)
            mst.append((a,b))
            graph[a].append(b)
            graph[b].append(a)
            mw += w
        print(mst)
        print(parents)
        print(ranks)
    return mw

print(MST_KRUSKAL(hl))