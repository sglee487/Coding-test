import sys
sys.setrecursionlimit(10**9)
from collections import deque


sys.stdin = open("2468-안전 영역-1.txt", "r")

input = sys.stdin.readline

N = int(input())

MIN_HEIGHT = 101
MAX_HEIGHT = 0
city = []
not_water = deque()
for r in range(N):
    tmp = list(map(int, input().split()))
    MIN_HEIGHT = min(MIN_HEIGHT, min(tmp))
    MAX_HEIGHT = max(MAX_HEIGHT, max(tmp))
    for c, h in enumerate(tmp):
        not_water.append((r,c))
    city.append(tmp)

# print(*city,sep='\n')
# print(MIN_HEIGHT)
# print(MAX_HEIGHT)
#
# print(not_water)

# 위 오 아래 왼
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def make_group(r,c, gn, group,safe):
    gq = deque()
    gq.append((r,c))
    while gq:
        qr, qc = gq.pop()
        group[qr][qc] = gn
        for i in range(4):
            nr, nc = qr + dy[i], qc + dx[i]
            if not (0 <= nr < N and 0 <= nc < N): continue
            if group[nr][nc]: continue
            if not safe[nr][nc]: continue
            group[nr][nc] = gn
            gq.append((nr,nc))
    
gnmax = 0

safe = [[1] * N for _ in range(N)]
for rain in range(MIN_HEIGHT-1, MAX_HEIGHT):
    for (r, c) in list(not_water):
        if city[r][c] == rain:
            safe[r][c] = 0
            not_water.remove((r,c))
    group = [[0] * N for _ in range(N)]
    gn = 0
    for (r, c) in list(not_water):
        if group[r][c] == 0:
            gn += 1
            make_group(r,c,gn,group,safe)
    # print("rain", rain)
    # print(*safe, sep='\n')
    # print()
    # print(*group, sep='\n')
    # print(gn)
    gnmax = max(gnmax, gn)
# print(not_water)
print(gnmax)