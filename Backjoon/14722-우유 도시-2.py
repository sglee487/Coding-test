import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("14722-우유 도시-2.txt", "r")

input = sys.stdin.readline

N = int(input())

city = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

if city[0][0] == 0:
    dp[0][0] = 1

for r in range(1, N):
    dp[r][0] = dp[r - 1][0]
    if city[r][0] == dp[r][0] % 3:
        dp[r][0] += 1

for c in range(1, N):
    dp[0][c] = dp[0][c - 1]
    if city[0][c] == dp[0][c] % 3:
        dp[0][c] += 1

for r in range(1, N):
    for c in range(1, N):
        dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        if city[r][c] == dp[r][c] % 3:
            dp[r][c] += 1

print(dp[N-1][N-1])