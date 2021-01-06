import sys

sys.stdin = open("DP-바닥 공사.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    dp = [0] * (N+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    for i in range(3,N+1):
        dp[i] = (2*dp[i-2] + dp[i-1])%796796
    print(dp)