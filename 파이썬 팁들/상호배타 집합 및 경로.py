# 파이썬 SW문제해결 응용_구현 - 06 그래프의 기본과 탐색

# 상호배타 집합 트리 (크루스칼 알고리즘)
# 유일한 원소 x를 포함하는 새로운 집합을 생성하는 연산
def Make_Set(x):
    p[x] = x

# x를 포함하는 집합을 찾는 연산
def Find_Set(x):
    if x == p[x]:
        return x
    else:
        return Find_Set(p[x])

# x와 y를 포함하는 두 집합을 통합하는 연산
def Union(x, y):
    p[Find_Set(y)] = Find_Set(x)

# 효율성을 고려해서 작성된 알고리즘 (크루스칼 알고리즘)
# p[x]: 노드 x의 부모 저장
# rank[x] : 루트 노드가 x인 트리의 랭크 값 저장

def Make_Set(x):
    p[x] = x # 자기 자신
    rank[x] = 0

def Find_Set(x):
    if x != p[x]: # x가 루트가 아닌 경우
        p[x] = Find_Set(p[x]) # Path Compression
    return p[x]

def Union(x,y):
    Link(Find_Set(x), Find_Set(y))

def Link(x,y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1

# 파이썬 SW문제해결 응용_구현 - 07 그래프의 최소 비용 문제
def MST_KRUSKAL(G):
    global mst_cost
    mst = []

    for i in range(N+1):
        Make_Set(i)

    G.sort(key = lambda t: t[2])

    # mst_cost = 0

    while len(mst) < N:
    # while G:
        u, v, val = G.pop(0)
        if Find_Set(u) != Find_Set(v):
            Union(u,v)
            mst.append((u,v))
            mst_cost += val

# 다익스트라 알고리즘
# D: 출발점에서 각 정점까지 최단 경로 가중치 합을 저장
# P: 최단 경로 트리 저장
def Dijkstra(G, r):
    D = [INF] * N
    P = [None] * N
    visited = [False] * N
    D[r] = 0

    for _ in range(N):
        minIndex = -1
        min = INF
        for i in range(N):
            if not visited[i] and D[i] < min:
                min = D[i]
                minIndex = i
        visited[minIndex] = True
        for v, val in G[minIndex]:
            if not visited[v] and D[minIndex] + val < D[v]:
                D[v] = D[minIndex] + val
                P[v] = minIndex

# 파이썬 SW문제해결 응용_최적화 - 04 동적계획법의 활용

# 모든 쌍 최단 경로 알고리즘 (플로이드-워샬 알고리즘)
# D[i][j]: i에서 j로 가는 최단 경로 가중치 합
# 최초 D[i][j]에는 간선(i,j)의 가중치 저장, i에서 j로 간선이 없으면 INF
def AllPairsShortest(D):
    for k in range(1, N+1):
        for i in range(1, n+1):
            if i == k: continue
            for j in range(1,n+1):
                if j == k or j == i: continue
                D[i][j] = min(D[i][k] + D[k][j], D[i][j])

# 순회 외판원 문제에 대한 동적 계획법 알고리즘
# W: 인접 행렬, minlength: 최적일주여행경로의 가중치 합, n: 정점의 개수
# D: 부분 문제의 해를 저장하기 위한 저장소
def travel(n, W):
    number D[1..n][subset of V - {v1}]

    for i in 2 -> n:
        D[i][emptyset] <- W[i][1]

    for k in 1 -> n - 2:
        for all subsets A <= V - {v1} containing k vertices:
            for i such that i!=1 and vi !<= A:
                D[i][A] = minimum(vj<=A)(W[i][j] + D[vj][A - {vj}])

    D[1][V - {v1}] = minimum(2<=j<=n)(W[1][j] + D[vj][A - {v1}])
    minlength = D[1][V - {v1}]