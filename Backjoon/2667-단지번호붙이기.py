from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2667-단지번호붙이기-1.txt", "r")

input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().strip())) for _ in range(N)]

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

visited = [[False] * N for _ in range(N)]

def dfs(r,c):
    size = 1
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not (0<=nr<N and 0<=nc<N): continue
        if maps[nr][nc] != 1 or visited[nr][nc]: continue
        visited[nr][nc] = True
        size += dfs(nr,nc)
    return size

danjil = []
for r in range(N):
    for c in range(N):
        if maps[r][c] == 1 and not visited[r][c]:
            visited[r][c] = True
            danjil.append(dfs(r,c))

print(len(danjil))
danjil.sort()
print(*danjil, sep='\n')