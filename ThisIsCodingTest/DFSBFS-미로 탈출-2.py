from collections import deque
import sys

sys.stdin = open("DFSBFS-미로 탈출.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())

miro = [list(map(int, input().strip())) for _ in range(N)]

# 위 오 아래 왼
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

visited = [[False] * M for _ in range(N)]
Q = deque()
Q.append((0, 0, 1))
visited[0][0] = True

while Q:
    r, c, step = Q.popleft()
    if (r, c) == (N - 1, M - 1):
        print(step)
        exit()
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not (0 <= nr < N and 0 <= nc < M): continue
        if miro[nr][nc] != 1: continue
        if visited[nr][nc]: continue
        visited[nr][nc] = True
        Q.append((nr, nc, step + 1))


