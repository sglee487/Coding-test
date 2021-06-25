import sys
import math
sys.setrecursionlimit(10**9)

sys.stdin = open("2193-이친수-5.txt", "r")

input = sys.stdin.readline

N = int(input())

if N <= 2:
    print(1)
    exit()
if N == 3:
    print(2)
    exit()

dp = [0] * (N+1)
dp[1] = 1
dp[2] = 1
dp[3] = 2

for i in range(4, N+1):
    dp[i] += 1
    for j in range(i-2,0,-1):
        dp[i] += dp[j]
print(dp[N])