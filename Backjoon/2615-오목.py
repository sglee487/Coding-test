# -*- coding: utf-8 -*-
import copy
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2615-오목-7.txt", "r")

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]
visited = [[0] * 19 for _ in range(19)]

# # 위 위오 오 오아 아 왼아 왼 왼위
# dy = [-1,-1,0,1,1,1,0,-1]
# dx = [0,1,1,1,0,-1,-1,-1]

# 오 오아 아 오위
dy = [0,1,1, -1]
dx = [1,1,0, 1]

def has_winner(step, r,c,dol):
    visited[r][c] |= (1 << dol)
    visited[r][c] |= (1 << 3)
    visited[r][c] |= (1 << 4)
    visited[r][c] |= (1 << 5)
    visited[r][c] |= (1 << 6)

    # 오른쪽 길이. bit 3
    l = 1
    nc = c
    while True:
        nc = nc + dx[0]
        if nc < 19 and board[r][nc] == dol:
            if (1 << dol) & visited[r][nc] == 0 or \
                (1 << 3) & visited[r][nc] == 0: 
                visited[r][nc] |= (1 << dol)
                visited[r][nc] |= (1 << 3)
                l += 1
            else:
                l = 99
                break
        else:
            break

    if l == 5:
        return True

    # 오른쪽 아래 길이. bit 4
    l = 1
    nr, nc = r, c
    while True:
        nr, nc = nr + dy[1], nc + dx[1]
        if nr < 19 and nc < 19 and board[nr][nc] == dol:
            if (1 << dol) & visited[nr][nc] == 0 or \
                (1 << 4) & visited[nr][nc] == 0: 
                visited[nr][nc] |= (1 << dol)
                visited[nr][nc] |= (1 << 4)
                l += 1
            else:
                l = 99
                break
        else:
            break

    if l == 5:
            return True

    # 아래 길이. bit 5
    l = 1
    nr = r
    while True:
        nr = nr + dy[2]
        if nr < 19 and board[nr][c] == dol:
            if (1 << dol) & visited[nr][c] == 0 or \
                (1 << 5) & visited[nr][c] == 0: 
                visited[nr][c] |= (1 << dol)
                visited[nr][c] |= (1 << 5)
                l += 1
            else:
                l = 99
                break
        else:
            break

    if l == 5:
        return True

    # 오위 길이. bit 6
    l = 1
    nr, nc = r, c
    while True:
        nr, nc = nr + dy[3], nc + dx[3]
        if 0<=nr < 19 and 0<=nc < 19 and board[nr][nc] == dol:
            if (1 << dol) & visited[nr][nc] == 0 or \
                (1 << 6) & visited[nr][nc] == 0: 
                visited[nr][nc] |= (1 << dol)
                visited[nr][nc] |= (1 << 6)
                l += 1
            else:
                l = 99
                break
        else:
            break

    if l == 5:
        return True

    return False


def start():
    for c in range(19):
        for r in range(19):
            if board[r][c]:
                if has_winner(1,r,c,board[r][c]):
                    return board[r][c], r, c
    
    return 0, -1, -1

winner, r, c = start()
print(winner)
if winner > 0:
    print(r+1,c+1)