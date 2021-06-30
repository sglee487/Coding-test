import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("11057-오르막 수-3.txt", "r")

# input = sys.stdin.readline

N = int(input())
dp = [[0] * 11 for _ in range(N)]
dp[0] = [1] * 10 + [10]
for i in range(1, N):
    total = dp[i-1][10]
    dp[i][0] = total
    all_sum = total
    for j in range(1, 10):
        total -= dp[i-1][j-1]
        dp[i][j] = total
        all_sum += total
    dp[i][10] = all_sum

print(dp[N-1][10] % 10007)