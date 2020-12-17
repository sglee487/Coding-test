import sys
from collections import deque

sys.stdin = open("그래프 이론-행성 터널 1.txt", "r")
# https://github.com/ndb796/python-for-coding-test/blob/master/10/5.py
input = sys.stdin.readline # 꼭 sys.stdin 밑에
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
planets = [list(map(int, input().split())) for _ in range(N)]
# print(planets)
parent = list(range(N))
xp = []
yp = []
zp = []
for i,p in enumerate(planets):
    xp.append((p[0],i))
    yp.append((p[1], i))
    zp.append((p[2], i))
xp.sort()
yp.sort()
zp.sort()
# print(xp)
# print(yp)
# print(zp)
distances = []
for i in range(len(planets)-1):
    xd = abs(xp[i][0]-xp[i+1][0])
    distances.append((xd,xp[i][1],xp[i+1][1]))
    yd = abs(yp[i][0]-yp[i+1][0])
    distances.append((yd,yp[i][1],yp[i+1][1]))
    zd = abs(zp[i][0]-zp[i+1][0])
    distances.append((zd,zp[i][1],zp[i+1][1]))
distances.sort()
# print(distances)
distances = deque(distances)

result = 0
while distances:
    d, i, j = distances.popleft()
    if find_parent(parent,i) != find_parent(parent,j):
        result += d
        union_parent(parent,i,j)
print(result)