# https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3

from collections import deque

def solution(board):
    N = len(board)
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    result = 10e9
    Q = deque()
    board[0][0] = 1
    Q.append((0,0,1,0))
    Q.append((0,0,2,0))
    costmatrix = [[10e9] * N for _ in range(N)]
    costmatrix[0][0] = 0
    while Q:
        r, c, d, cost = Q.popleft()
        if (r,c) == (N-1,N-1):
            result = min(result,cost)
            continue
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if not (0<=nr<N and 0<=nc<N): continue
            if board[nr][nc] == 1: continue
            if i == d:
                if costmatrix[nr][nc] < cost+100: continue
                costmatrix[nr][nc] = cost+100
                Q.append((nr,nc,d, cost+100))
            elif ((i+2) % 4) == d:
                continue
            else:
                if costmatrix[nr][nc] < cost+600: continue
                costmatrix[nr][nc] = cost+600
                Q.append((nr,nc,i, cost+600))

    return result

