# https://www.acmicpc.net/problem/14502
from collections import deque
import sys
import copy

# 밑은 백준용 읽기 코드
# import sys
# input = sys.stdin.readline

sys.stdin = open("DFSBFS-연구소.txt", "r")


def spread(dfsboard):
    tobespreadboard = copy.deepcopy(dfsboard)
    Q = deque()
    for r in range(N):
        for c in range(M):
            if tobespreadboard[r][c] == 2:
                Q.append((r, c))
    while Q:
        r, c = Q.pop()
        if 0 <= c - 1:
            # 왼
            if tobespreadboard[r][c - 1] == 0:
                tobespreadboard[r][c - 1] = 2
                Q.append((r, c - 1))
        if 0 <= r - 1:
            # 위
            if tobespreadboard[r-1][c] == 0:
                tobespreadboard[r - 1][c] = 2
                Q.append((r - 1, c))
        if c + 1 < M:
            # 오
            if tobespreadboard[r][c+1] == 0:
                tobespreadboard[r][c + 1] = 2
                Q.append((r, c + 1))
        if r + 1 < N:
            # 아래
            if tobespreadboard[r+1][c] == 0:
                tobespreadboard[r + 1][c] = 2
                Q.append((r + 1, c))
    return tobespreadboard


def count0(dfsboard):
    count = 0
    for r in range(N):
        for c in range(M):
            if dfsboard[r][c] == 0:
                count += 1
    return count


def dfs(n, dfsboard):
    global result
    if n < 3:
        for r in range(N):
            for c in range(M):
                if dfsboard[r][c] == 0:
                    dfsboard[r][c] = 1
                    dfs(n + 1, dfsboard)
                    dfsboard[r][c] = 0
    else:
        spreadboard = spread(dfsboard)
        cleanrooms = count0(spreadboard)
        if cleanrooms > result:
            result = cleanrooms

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    # print(*board,sep='\n')

    result = 0
    dfs(0,board)
    print(result)