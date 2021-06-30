import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("10844-쉬운 계단 수-3.txt", "r")

input = sys.stdin.readline

N = int(input())

dp = [[0] * (N+1) for _ in range(10)]
for i in range(1,10):
    dp[i][1] = 1

for j in range(2,N+1):
    for i in range(10):
        if i-1 >= 0:
            dp[i][j] += dp[i-1][j-1]
        if i+1 <= 9:
            dp[i][j] += dp[i+1][j-1]

answer = 0
for i in range(10):
    answer += dp[i][N]
print(answer)