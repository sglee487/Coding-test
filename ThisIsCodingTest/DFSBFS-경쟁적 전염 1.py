from collections import deque
import sys

sys.stdin = open("DFSBFS-경쟁적 전염2.txt", "r")

T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, K = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    S, R, C = map(int, sys.stdin.readline().split())
    # print(*board,sep='\n')
    t = 0
    QList = [deque() for _ in range(K+1)]
    for r in range(N):
        for c in range(N):
            if board[r][c] != 0:
                QList[board[r][c]].append((r,c,0))

    # 위, 오른쪽, 아래, 왼쪽
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    while t < S:
        for i, Q in enumerate(QList):
            while Q and Q[0][2] == t:
                r,c,t = Q.popleft()
                for d in range(4):
                    nr, nc = r + dy[d], c + dx[d]
                    if 0<=nr<N and 0<= nc<N and board[nr][nc] == 0:
                        board[nr][nc] = i
                        QList[i].append((nr,nc,t+1))
        t += 1
    # print(*board, sep='\n')
    print(board[R-1][C-1])