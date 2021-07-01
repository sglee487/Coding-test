from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("1012-유기농 배추-2.txt", "r")

input = sys.stdin.readline

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def dfs(farm, warms, r, c, warm):
    global M,N
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not (0<=nr<N and 0<=nc<M): continue
        if farm[nr][nc] == 0 or warms[nr][nc] != 0: continue
        warms[nr][nc] = warm
        dfs(farm, warms, nr, nc, warm)

    return

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    warms = [[0] * M for _ in range(N)]
    for _ in range(K):
        m, n = map(int, input().split())
        farm[n][m] = 1

    warm = 0
    for r in range(N):
        for c in range(M):
            if farm[r][c] == 1 and warms[r][c] == 0:
                warm += 1
                dfs(farm,warms,r,c,warm)

    print(warm)