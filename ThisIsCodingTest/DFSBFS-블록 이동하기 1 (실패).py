# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque

def solution(board):
    print(*board,sep='\n')
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    N = len(board)
    def ispossible(r1, c1, r2, c2):
        if (0 <= r1 < N and 0 <= c1 < N and 0 <= r2 < N and 0 <= c2 < N
                and board[r1][c1] == 0 and board[r2][c2] == 0):
            return True
        return False

    Q = deque()
    Q.append((0,0,0))
    Q.append((0,1,0))
    visited = [[False] * N for _ in range(N)]
    step = 0
    while Q:
        # 가로일 땐 r1,c1 가 왼쪽 r2,c2 가 오른쪽
        # 세로일 땐 r1,c1 가 위, r2,c2가 아래
        # print(Q)
        r1,c1,m = Q.popleft()
        r2,c2,m = Q.popleft()
        if m == 15: break
        if (r1,c1) == (N-1,N-1) or (r2,c2) == (N-1,N-1):
            step = m
            break
        if visited[r1][c1] and visited[r2][c2]: continue
        visited[r1][c1] = True
        visited[r2][c2] = True
        board[r1][c1] = 3
        board[r2][c2] = 3
        print(*board, sep='\n')
        print(r1, c1, r2, c2, m)
        board[r1][c1] = 0
        board[r2][c2] = 0
        for i in range(4):
            nr1, nc1 = r1 + dy[i], c1 + dx[i]
            nr2, nc2 = r2 + dy[i], c2 + dx[i]
            if ispossible(nr1,nc1,nr2,nc2):
                Q.append((nr1,nc1,m+1))
                Q.append((nr2,nc2,m+1))
        if r1 == r2:
            # 가로
            # 오른쪽을 왼쪽 위로
            if 0<=r2-1 and board[r2-1][c2] == 0 and board[r1-1][c1] == 0:
                Q.append((r2 - 1, c1,m+1))
                Q.append((r1,c1,m+1))
            # 오른쪽을 왼쪽 아래로
            if r2+1<N and board[r2+1][c2] == 0 and board[r1+1][c1] == 0:
                Q.append((r1,c1,m+1))
                Q.append((r1+1,c1,m+1))
            # 왼쪽을 오른쪽 위로
            if 0<=r1-1 and board[r1-1][c1] == 0 and board[r2-1][c2] == 0:
                Q.append((r2-1,c2,m+1))
                Q.append((r2,c2,m+1))
            # 왼쪽을 오른쪽 아래로
            if r1+1<N and board[r1+1][c1] == 0 and board[r2+1][c2] == 0:
                Q.append((r2,c2,m+1))
                Q.append((r2+1,c2,m+1))
        if c1 == c2:
            # 세로
            # 아래쪽을 위 왼쪽으로
            if 0<=c2-1 and board[r2][c2-1] == 0 and board[r1][c2-1] == 0:
                Q.append((r1,c2-1,m+1))
                Q.append((r1,c2,m+1))
            # 아래쪽을 위 오른쪽으로
            if c2+1<N and board[r2][c2+1] == 0 and board[r1][c2+1] == 0:
                Q.append((r1,c1,m+1))
                Q.append((r1,c2+1,m+1))
            # 위쪽을 아래 왼쪽으로
            if 0<=c1-1 and board[r1][c1-1] == 0 and board[r2][c1-1] == 0:
                Q.append((r2,c1-1,m+1))
                Q.append((r2,c2,m+1))
            # 위쪽을 아래 오른쪽으로
            if c2+1<N and board[r1][c1+1] == 0 and board[r2][c2+1] == 0:
                Q.append((r2,c2,m+1))
                Q.append((r2,c2+1,m+1))

    return step

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]),7)