# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque
import numpy as np

def solution(board):
    N = len(board)
    boardextend = np.array([[1]*(N+2) for _ in range(N+2)])
    boardextend[1:N+1,1:N+1] = board
    # print(*boardextend,sep='\n')

    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    Q = deque()
    visited = []
    Q.append(((1,1),(1,2),0))
    visited.append({(1,1),(1,2)})
    result = int()
    while Q:
        (r1,c1),(r2,c2),t = Q.popleft()
        if (r1,c1) == (N,N) or (r2,c2) == (N,N):
            result = t
            break
        # 위 오 아래 왼 이동
        for i in range(4):
            nr1,nc1,nr2,nc2 = r1+dy[i],c1+dx[i],r2+dy[i],c2+dx[i]
            if boardextend[nr1][nc1] == 1 or boardextend[nr2][nc2] == 1: continue
            if {(nr1,nc1),(nr2,nc2)} in visited: continue
            Q.append(((nr1,nc1),(nr2,nc2),t+1))
            visited.append({(nr1,nc1),(nr2,nc2)})
        # 회전
        # 가로일 경우
        if r1 == r2:
            #위
            if boardextend[r1-1][c1] == 0 and boardextend[r2-1][c2] == 0:
                if {(r1,c1),(r1-1,c1)} not in visited:
                    Q.append(((r1,c1),(r1-1,c1),t+1))
                    visited.append({(r1, c1), (r1 - 1, c1)})
                if {(r2,c2),(r2-1,c2)} not in visited:
                    Q.append(((r2, c2), (r2 - 1, c2), t + 1))
                    visited.append({(r2,c2),(r2-1,c2)})
            #아래
            if boardextend[r1+1][c1] == 0 and boardextend[r2+1][c2] == 0:
                if {(r1,c1),(r1+1,c1)} not in visited:
                    Q.append(((r1,c1),(r1+1,c1),t+1))
                    visited.append({(r1, c1), (r1 + 1, c1)})
                if {(r2,c2),(r2+1,c2)} not in visited:
                    Q.append(((r2,c2),(r2+1,c2),t+1))
                    visited.append({(r2,c2),(r2+1,c2)})
        # 세로일 경우
        if c1 == c2:
            #오른쪽
            if boardextend[r1][c1+1] == 0 and boardextend[r2][c2+1] == 0:
                if {(r1, c1), (r1, c1+1)} not in visited:
                    Q.append(((r1, c1), (r1, c1+1),t+1))
                    visited.append({(r1, c1), (r1, c1 + 1)})
                if {(r2, c2), (r2, c2+1)} not in visited:
                    Q.append(((r2, c2), (r2, c2 + 1), t + 1))
                    visited.append({(r2, c2), (r2, c2+1)})
            #왼쪽
            if boardextend[r1][c1-1] == 0 and boardextend[r2][c2-1] == 0:
                if {(r1, c1), (r1, c1-1)} not in visited:
                    Q.append(((r1, c1), (r1, c1-1),t+1))
                    visited.append({(r1, c1), (r1, c1 - 1)})
                if {(r2, c2), (r2, c2-1)} not in visited:
                    Q.append(((r2, c2), (r2, c2-1),t+1))
                    visited.append({(r2, c2), (r2, c2-1)})
    return result


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]),7)
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]),21)
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]),11)
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]),33)