import sys

sys.stdin = open("sample_input.txt", "r")

# 상호배타 집합 트리
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


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, E = map(int, input().split())
    G = []
    for _ in range(E):
        il = list(map(int, input().split()))
        G.append((il[0],il[1],il[2]))

    p = [0] * (N+1)
    rank = [0] * (N+1)
    mst_cost = 0
    MST_KRUSKAL(G)

    print("#{}".format(test_case),mst_cost)

    # ///////////////////////////////////////////////////////////////////////////////////
