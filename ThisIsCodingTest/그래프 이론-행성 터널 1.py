import sys

sys.stdin = open("그래프 이론-행성 터널 1.txt", "r")
# https://github.com/ndb796/python-for-coding-test/blob/master/10/5.py

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
edges = []
allcost = 0
for _ in range(M):
    a, b, cost = map(int, input().split())
    allcost += cost
    edges.append((cost,a,b))
edges.sort()
parent = list(range(N))
usedcost = 0
for cost, a, b in edges:
    if find_parent(parent,a) != find_parent(parent,b):
        usedcost += cost
        union_parent(parent,a,b)
print(allcost-usedcost)