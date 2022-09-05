from collections import deque

import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("1743-음식물 피하기-1.txt", "r")

input = sys.stdin.readline

N, M, K = map(int, input().split())

board = [['.'] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = '#'

answer = 0
visited = [[False] * M for _ in range(N)]

# 위 오 아래 왼
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def trash_gush(r, c):
    global board, visited, N, M, answer, local_size
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not (0 <= nr < N and 0 <= nc < M): continue
        if visited[nr][nc] or board[nr][nc] != '#': continue
        visited[nr][nc] = True
        local_size += 1
        trash_gush(nr, nc)


for r in range(N):
    for c in range(M):
        local_size = 0
        if not visited[r][c] and board[r][c] == '#':
            visited[r][c] = True
            local_size += 1
            trash_gush(r, c)
        answer = max(answer, local_size)

print(answer)
