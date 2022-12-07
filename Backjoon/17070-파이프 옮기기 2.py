import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("17070-파이프 옮기기 1-4.txt", "r")

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 가로:0, 세로:1, 대각선:2
dp = [[[-1] * 3 for _ in range(N)] for _ in range(N)]


def dfs(r, c, d):
    if (r, c) == (N - 1, N - 1):
        return 1
    if dp[r][c][d] != -1:
        return dp[r][c][d]
    dp[r][c][d] = 0
    if d == 0:
        if c + 1 < N and board[r][c + 1] == 0:
            dp[r][c][d] += dfs(r, c + 1, 0)
        if r + 1 < N and c + 1 < N and board[r][c + 1] == 0 and board[r + 1][c] == 0 and board[r + 1][c + 1] == 0:
            dp[r][c][d] += dfs(r + 1, c + 1, 2)
    if d == 1:
        if r + 1 < N and board[r + 1][c] == 0:
            dp[r][c][d] += dfs(r + 1, c, 1)
        if r + 1 < N and c + 1 < N and board[r][c + 1] == 0 and board[r + 1][c] == 0 and board[r + 1][c + 1] == 0:
            dp[r][c][d] += dfs(r + 1, c + 1, 2)
    if d == 2:
        if c + 1 < N and board[r][c + 1] == 0:
            dp[r][c][d] += dfs(r, c + 1, 0)
        if r + 1 < N and board[r + 1][c] == 0:
            dp[r][c][d] += dfs(r + 1, c, 1)
        if r + 1 < N and c + 1 < N and board[r][c + 1] == 0 and board[r + 1][c] == 0 and board[r + 1][c + 1] == 0:
            dp[r][c][d] += dfs(r + 1, c + 1, 2)
    return dp[r][c][d]


print(dfs(0, 1, 0))
