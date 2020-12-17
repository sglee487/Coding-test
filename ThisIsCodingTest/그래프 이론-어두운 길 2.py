import sys
from collections import deque

sys.stdin = open("그래프 이론-어두운 길 1.txt", "r")
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

N, M = map(int, input().split())
edges = []
alld = 0
for _ in range(M):
    X, Y, Z = map(int, input().split())
    edges.append((Z,X,Y))
    alld += Z
edges.sort()
edges = deque(edges)
parent = list(range(N))
cond = 0
while edges:
    d, x, y = edges.popleft()
    if find_parent(parent,x) != find_parent(parent,y):
        union_parent(parent,x,y)
        cond += d
print(alld - cond)