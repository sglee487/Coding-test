from collections import deque
import copy
import sys

sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # print(*board,sep='\n')

    cores = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1: cores.append((r,c))
    # print(cores)

    CN = len(cores)

    gcore = 0
    gways = 99999999
    # 위 오른쪽 아래 왼쪽
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    Q = deque()
    Q.append((0,0,0,copy.deepcopy(board)))
    while Q:
        coreindex, corecount, totalways, copyedboard = Q.pop()
        if coreindex == CN:
            if corecount >= gcore:
                if gcore == corecount:
                    gways = min(totalways,gways)
                else:
                    gcore = corecount
                    gways = totalways
        else:
            r, c = cores[coreindex]
            if r == 0 or r == N-1 or c == 0 or c == N-1:
                Q.append((coreindex+1, corecount + 1, totalways, copy.deepcopy(copyedboard)))
            else:
                for i in range(4):
                    newboard = copy.deepcopy(copyedboard)
                    nr, nc = r + dy[i], c + dx[i]
                    can_be_connected = bool()
                    while 0<=nr<N and 0<=nc<N and newboard[nr][nc] == 0:
                        nr, nc = nr + dy[i], nc + dx[i]
                    if nr == -1 or nr == N or nc == -1 or nc == N: can_be_connected = True
                    else: can_be_connected = False
                    if can_be_connected:
                        nr, nc = r + dy[i], c + dx[i]
                        way = 0
                        while 0 <= nr < N and 0 <= nc < N and newboard[nr][nc] == 0:
                            newboard[nr][nc] = N + coreindex
                            nr, nc = nr + dy[i], nc + dx[i]
                            way += 1
                        Q.append((coreindex+1, corecount + 1, totalways + way, copy.deepcopy(newboard)))
                    else:
                        Q.append((coreindex + 1, corecount, totalways, copy.deepcopy(newboard)))

    # print(gcore,gways)
    print("#{}".format(test_case),gways)