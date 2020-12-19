import sys

sys.stdin = open("그래프 이론-행성 터널 1.txt", "r")

# https://github.com/ndb796/Python-Competitive-Programming-Team-Notes/blob/master/Data%20Structure/disjoint_set.py
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
planets = [tuple(map(int, input().split())) for _ in range(N)]
# print(*planets,sep='\n')
planetsX = []
planetsY = []
planetsZ = []
for i, (x, y, z) in enumerate(planets):
    planetsX.append((x,i))
    planetsY.append((y, i))
    planetsZ.append((z, i))
planetsX.sort()
planetsY.sort()
planetsZ.sort()
# print(planetsX)
# print(planetsY)
# print(planetsZ)
distances = []
for i in range(N-1):
    distances.append((planetsX[i+1][0]-planetsX[i][0],planetsX[i+1][1],planetsX[i][1]))
    distances.append((planetsY[i+1][0]-planetsY[i][0],planetsY[i+1][1],planetsY[i][1]))
    distances.append((planetsZ[i+1][0]-planetsZ[i][0],planetsZ[i+1][1],planetsZ[i][1]))
parent = list(range(N))
distances.sort()
result = 0
for dist, a, b in distances:
    if find_parent(parent,a) != find_parent(parent,b):
        result += dist
        union_parent(parent,a,b)
        # print(parent,result)
print(result)