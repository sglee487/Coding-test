from collections import deque
import sys

sys.stdin = open("DFSBFS-음료수 얼려먹기.txt", "r")

def process(r,c):
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    Q = deque()
    Q.append((r,c))
    union[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0<=nr<N and 0<=nc<M and board[nr][nc] == 0 and union[nr][nc] == 0:
                Q.append((nr,nc))
                union[nr][nc] = 1
    return

T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int,input())) for _ in range(N)]
    print(*board,sep='\n')

    union = [[0] * M for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0 and union[r][c] == 0:
                process(r,c)
                result += 1
    print(result)