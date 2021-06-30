import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("11052-카드 구매하기-6.txt", "r")

input = sys.stdin.readline

N = int(input())
cl = list(map(int, input().split()))
dp = [[0] * (N+1) for _ in range(N+1)]
cl.insert(0,0)
for i in range(1, N+1):
    for j in range(1, N+1):
        d, r = divmod(j, i)
        dp[i][j] = max(cl[i] * d, dp[i][j-r] + dp[i-1][r], dp[i-1][j])

print(dp[N][N])