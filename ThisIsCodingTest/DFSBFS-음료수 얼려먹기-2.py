import sys

sys.stdin = open("DFSBFS-음료수 얼려먹기-2.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(N)]

group = [[0] * M for _ in range(N)]
group_num = 0

# 위 오 아래 왼
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def fill_group(r, c, group_num):
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not (0 <= nr < N and 0 <= nc < M): continue
        if board[nr][nc] == 1: continue
        if group[nr][nc] != 0: continue
        group[nr][nc] = group_num
        fill_group(nr, nc, group_num)


for r in range(N):
    for c in range(M):
        if board[r][c] == 0 and group[r][c] == 0:
            group_num += 1
            group[r][c] = group_num
            fill_group(r, c, group_num)

print(group_num)
