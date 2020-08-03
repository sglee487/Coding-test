from collections import deque
import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())

    board = [[0] * (N+1) for _ in range(N+1)]

    for i in range(N+1):
        board[0][i] = 3
        board[i][0] = 3

    # 1 이 흑. 2 가 백.
    board[N//2][N//2] = 2
    board[N // 2][(N // 2)+1] = 1
    board[(N // 2)+1][N // 2] = 1
    board[(N // 2)+1][(N // 2)+1] = 2

    # print(*board,sep='\n')

    # 아래, 우측아래, 우측, 우측위, 위, 좌측위, 좌측, 좌측아래
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    Q = deque()

    for _ in range(M):
        c, r, color = map(int, input().split())
        board[r][c] = color
        if color == 1:
            for d in range(8):
                x, y = c, r
                x += dx[d]
                y += dy[d]
                while 1 <= x <= N and 1 <= y <= N:
                    if board[y][x] == 2:
                        Q.append((x,y))
                    if board[y][x] == 1:
                        while Q:
                            x, y = Q.pop()
                            board[y][x] = 1
                        break
                    x += dx[d]
                    y += dy[d]
                Q.clear()
        if color == 2:
            for d in range(8):
                x, y = c, r
                x += dx[d]
                y += dy[d]
                while 1 <= x <= N and 1 <= y <= N:
                    if board[y][x] == 1:
                        Q.append((x,y))
                    if board[y][x] == 2:
                        while Q:
                            x, y = Q.pop()
                            board[y][x] = 2
                        break
                    x += dx[d]
                    y += dy[d]
                Q.clear()
        # board[r][c] = color
        # print(r,c,color)
        # print(*board, sep='\n')

    # print()
    # print(*board,sep='\n')
    bc = 0
    wc = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if board[i][j] == 1: bc += 1
            if board[i][j] == 2: wc += 1


    print("#{}".format(test_case),bc,wc)
    # ///////////////////////////////////////////////////////////////////////////////////
