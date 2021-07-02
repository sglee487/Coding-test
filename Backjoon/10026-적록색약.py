import sys
sys.setrecursionlimit(10 ** 9)

sys.stdin = open("10026-적록색약-1.txt", "r")

input = sys.stdin.readline

N = int(input())
maps = [list(input().strip()) for _ in range(N)]

visited_normal = [[False] * N for _ in range(N)]
visited_blind = [[False] * N for _ in range(N)]

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(r, c, color, normal):
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not (0<=nr<N and 0<=nc<N): continue
        if normal:
            if maps[nr][nc] != color: continue
            if visited_normal[nr][nc]: continue
            visited_normal[nr][nc] = True
            dfs(nr,nc,color,normal)
        else:
            if color == 'R' or color == 'G':
                if maps[nr][nc] != 'R' and maps[nr][nc] != 'G': continue
            else:
                if maps[nr][nc] != color: continue
            if visited_blind[nr][nc]: continue
            visited_blind[nr][nc] = True
            dfs(nr,nc,color,normal)

normal_group = 0
blind_group = 0
for r in range(N):
    for c in range(N):
        if not visited_normal[r][c]:
            visited_normal[r][c] = True
            normal_group += 1
            dfs(r,c,maps[r][c],True)
        if not visited_blind[r][c]:
            visited_blind[r][c] = True
            blind_group += 1
            dfs(r,c,maps[r][c],False)

print(normal_group, blind_group)
