import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("17070-파이프 옮기기 1-4.txt", "r")

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# print(*board, sep='\n')
dp = [[[0] * N for _ in range(N)] for _ in range(3)]

def dfs(now_r, now_c, now_degree):
    global N, board, dp
    if dp[now_degree][now_r][now_c] != 0:
        return dp[now_degree][now_r][now_c]
    dp[now_degree][now_r][now_c] = 0
    if (now_r, now_c) == (N-1, N-1):
        return 1
    if now_degree == 0:
        if now_c+1 < N and board[now_r][now_c+1] == 0:
            dp[now_degree][now_r][now_c] += dfs(now_r, now_c + 1, 0)
            if now_r+1 < N and board[now_r+1][now_c] == 0 and board[now_r+1][now_c+1] == 0:
                dp[now_degree][now_r][now_c] += dfs(now_r + 1, now_c + 1, 2)
    elif now_degree == 1:
        if now_r+1 < N and board[now_r+1][now_c] == 0:
            dp[now_degree][now_r][now_c] += dfs(now_r + 1, now_c, 1)
            if now_c+1 < N and board[now_r][now_c+1] == 0 and board[now_r+1][now_c+1] == 0:
                dp[now_degree][now_r][now_c] += dfs(now_r + 1, now_c + 1, 2)
    elif now_degree == 2:
        if now_c+1 < N and board[now_r][now_c+1] == 0:
            dp[now_degree][now_r][now_c] += dfs(now_r, now_c + 1, 0)
        if now_r + 1 < N and board[now_r + 1][now_c] == 0:
            dp[now_degree][now_r][now_c] += dfs(now_r + 1, now_c, 1)
            if now_c + 1 < N and board[now_r][now_c + 1] == 0 and board[now_r + 1][now_c + 1] == 0:
                dp[now_degree][now_r][now_c] += dfs(now_r + 1, now_c + 1, 2)
    return dp[now_degree][now_r][now_c]


count = dfs(0,1,0)

print(count)
# print(*dp, sep='\n')