from collections import deque

import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("1149-RGB거리-1.txt", "r")

input = sys.stdin.readline

def dfs(n, j):
    if dp[n][j] != -1:
        return dp[n][j]
    ret = 987654321
    for i in range(3):
        if i == j: continue
        ret = min(ret, RGB[n][j] + dfs(n-1, i))
    dp[n][j] = ret
    return dp[n][j]

N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * 3 for _ in range(N)]
dp[0] = RGB[0]
answer = 987654321
answer = min(answer, dfs(N-1,0))
answer = min(answer, dfs(N-1,1))
answer = min(answer, dfs(N-1,2))
print(answer)