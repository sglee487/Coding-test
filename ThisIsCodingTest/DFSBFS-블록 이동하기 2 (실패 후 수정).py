# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque

# https://github.com/ndb796/python-for-coding-test/blob/master/13/8.py

def get_nextpos(pos,new_board):
    nextposes = []
    pos = list(pos)
    pos1r, pos1c, pos2r, pos2c = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    for i in range(4):
        np1r, np1c, np2r, np2c = pos1r+dy[i], pos1c+dx[i], pos2r+dy[i], pos2c+dx[i]
        if new_board[np1r][np1c] == 0 and new_board[np2r][np2c] == 0:
            nextposes.append({(np1r,np1c),(np2r,np2c)})

    # 가로
    if pos1r == pos2r:
        # 위 아래
        for i in [-1,1]:
            if new_board[pos1r+i][pos1c] == 0 and new_board[pos2r+i][pos2c] == 0:
                nextposes.append({(pos1r+i,pos1c),(pos1r,pos1c)})
                nextposes.append({(pos2r + i, pos2c), (pos2r, pos2c)})
    # 세로
    if pos1c == pos2c:
        # 왼 오른
        for i in [-1,1]:
            if new_board[pos1r][pos1c+i] == 0 and new_board[pos2r][pos2c+i] == 0:
                nextposes.append({(pos1r,pos1c+i),(pos1r,pos1c)})
                nextposes.append({(pos2r, pos2c+i), (pos2r, pos2c)})

    return nextposes

def solution(board):
    N = len(board)

    new_board = [[1] * (N+2) for _ in range(N+2)]
    for r in range(N):
        for c in range(N):
            new_board[r+1][c+1] = board[r][c]

    pos = {(1,1),(1,2)}
    Q = deque()
    Q.append((pos,0))
    visited = []
    visited.append(pos)
    while Q:
        pos, step = Q.popleft()
        if (N,N) in pos:
            return step
        for next_pos in get_nextpos(pos, new_board):
            if next_pos not in visited:
                Q.append((next_pos, step + 1))
                visited.append(next_pos)

    return

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]),7)
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]),21)
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]),11)
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]),33)