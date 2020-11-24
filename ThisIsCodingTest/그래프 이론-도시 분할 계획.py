# https://www.acmicpc.net/problem/1647
import sys

sys.stdin = open("그래프 이론-도시 분할 계획.txt", "r")

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

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    p = list(range(N+1))
    rank = [0] * (N+1)
    edges = []
    for _ in range(M):
        a, b, cost = map(int, input().split())
        edges.append((cost,a,b))

    edges.sort()
    result = 0
    lastedge = -1
    for edge in edges:
        cost, a, b = edge
        if Find_Set(a) != Find_Set(b):
            Union(a,b)
            result += cost
            lastedge = max(cost,lastedge)
    result -= lastedge

    print(result)