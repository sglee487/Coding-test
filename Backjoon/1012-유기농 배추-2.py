from collections import deque

import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("1012-유기농 배추-1.txt", "r")

input = sys.stdin.readline

T = int(input())
for test_case in range(T):
    M, N, K = map(int, input().split())

    board = [[0] * M for _ in range(N)]

    for _ in range(K):
        c, r = map(int,input().split())
        board[r][c] = 1

    group = [[0] * M for _ in range(N)]

    group_len = 0

    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    def make_group(r,c, group_num):
        global M,N,K,board,group
        group[r][c] = group_num
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if not (0<=nr<N and 0<=nc<M): continue
            if board[nr][nc] == 0 or group[nr][nc] != 0: continue
            make_group(nr,nc,group_num)

    for r in range(N):
        for c in range(M):
            if board[r][c] == 1 and group[r][c] == 0:
                make_group(r,c, group_len+1)
                group_len += 1

    print(group_len)