import sys
from itertools import combinations
import copy
# https://www.acmicpc.net/problem/18428

sys.stdin = open("DFSBFS-감시 피하기.txt", "r")

def can_hide(board,teachers):
    global N
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    for tr,tc in teachers:
        for i in range(4):
            nr, nc = tr + dy[i], tc + dx[i]
            while 0<=nr<N and 0<=nc<N:
                if board[nr][nc] == 'X':
                    nr, nc = nr + dy[i], nc + dx[i]
                elif board[nr][nc] == 'S':
                    return False
                elif board[nr][nc] == 'T':
                    break
                elif board[nr][nc] == 'O':
                    break
    return True


T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N = int(input())
    Board = [list(sys.stdin.readline().split()) for _ in range(N)]
    # print(*Board,sep='\n')
    # print()
    Students = []
    Teachers = []
    Voids = []
    for r in range(N):
        for c in range(N):
            if Board[r][c] == 'S': Students.append((r,c))
            elif Board[r][c] == 'T': Teachers.append((r,c))
            elif Board[r][c] == 'X': Voids.append((r,c))
    result = False
    for comb in combinations(Voids,3):
        tboard = copy.deepcopy(Board)
        for cr,cc in comb:
            tboard[cr][cc] = 'O'
        # print(*tboard, sep='\n')
        result = can_hide(tboard,Teachers)
        if result: break
    if result: print("YES")
    else: print("NO")