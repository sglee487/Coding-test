import sys
sys.setrecursionlimit(10**9)


sys.stdin = open("2468-안전 영역-3.txt", "r")

input = sys.stdin.readline

N = int(input())
maps = []
MIN, MAX = 101, 0
for _ in range(N):
    r = list(map(int, input().split()))
    MIN = min(min(r), MIN)
    MAX = max(max(r), MAX)
    maps.append(r)

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(r, c, height, visited):
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not (0<=nr<N and 0<=nc<N): continue
        if maps[nr][nc] <= height or visited[nr][nc]: continue
        visited[nr][nc] = True
        dfs(nr,nc, height, visited)

    return

group_max = 0
for h in range(MIN, MAX):
    group = 0
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if maps[r][c] > h and not visited[r][c]:
                group += 1
                visited[r][c] = True
                dfs(r, c, h, visited)
    group_max = max(group_max, group)

print(group_max)