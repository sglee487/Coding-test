from collections import deque
import sys

sys.stdin = open("DFSBFS-음료수 얼려먹기.txt", "r")

def make_ice(board, r, c):
    Q = deque()
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    Q.append((r,c))
    board[r][c] = 1
    while Q:
        qr, qc = Q.popleft()
        for i in range(4):
            nr, nc = qr + dy[i], qc + dx[i]
            if (0<=nr<N and 0<=nc<M) and board[nr][nc] == 0:
                board[nr][nc] = 1
                Q.append((nr,nc))
    return


T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input())) for _ in range(N)]
    ices = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0:
                make_ice(board, r, c)
                ices += 1
    print(ices)