import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("11051-이항 계수 2.txt", "r")

# input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (N+2) for _ in range(N+1)]
dp[0][1] = 1
for r in range(1,N+1):
    for c in range(1, r+2):
        dp[r][c] = dp[r-1][c-1] + dp[r-1][c]

print(dp[N][K+1] % 10007)