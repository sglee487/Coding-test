import sys
from collections import deque
sys.setrecursionlimit(10**9)

sys.stdin = open("3987-보이저 1호-1.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())

StarSystem = [input().strip() for _ in range(N)]

# direction U, R, D, L, visited
history = [[[0, 0, 0, 0, 0] for _ in range(M)] for _ in range(N)]

sr, sc = map(int, input().split())
sr -= 1
sc -= 1

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

ways = [-1,-1,-1,-1]

def change_dir(nowr,nowc,nowd):
    if StarSystem[nowr][nowc] == '\\':
        if nowd == 0: return 3
        if nowd == 3: return 0
        if nowd == 1: return 2
        if nowd == 2: return 1
    elif StarSystem[nowr][nowc] == '/':
        if nowd == 1: return 0
        if nowd == 3: return 2
        if nowd == 2: return 3
        if nowd == 0: return 1
    else:
        return nowd

def go(Q):
    while Q:
        nowr, nowc, nowd, time = Q.pop()
        if history[nowr][nowc][nowd] and history[nowr][nowc][4]:
            return -2 # Voyager
        if StarSystem[nowr][nowc] == 'C':
            return time - 1
        history[nowr][nowc][nowd] = 1
        history[nowr][nowc][4] = time
        newd = change_dir(nowr, nowc, nowd)
        newr, newc = nowr + dy[newd], nowc + dx[newd]
        if (0<=newr<N and 0<=newc<M):
            Q.append((newr, newc, newd, time+1))
        else:
            return time


for i in range(4):
    Q = deque()
    Q.append((sr,sc,i,1))
    ways[i] = go(Q)
    history = [[[0, 0, 0, 0, 0] for _ in range(M)] for _ in range(N)]

dirdict = {0: 'U', 1:'R', 2:'D', 3:'L'}

result = ['U', 0]
for i, (way) in enumerate(ways):
    if way == -2: # Voyager
        result[0] = dirdict[i]
        result[1] = 'Voyager'
        break
    elif way > result[1]:
        result[0] = dirdict[i]
        result[1] = way

print(*result, sep='\n')