import sys

sys.stdin = open("그래프 이론-여행 계획.txt", "r")

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

N,M = map(int,input().split())
rank = [0] * (N+1)
p = list(range(N+1))
for a in range(1,N+1):
    for b, c in enumerate(map(int, input().split()),1):
        Union(a,b)

trav = list(map(int, input().split()))
poss = True
for i in range(len(trav)-1):
    if Find_Set(trav[i]) != Find_Set(trav[i+1]):
        poss = False
        break

if poss: print("YES")
else: print("NO")