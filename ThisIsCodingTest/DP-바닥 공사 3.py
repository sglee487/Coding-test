import sys

sys.stdin = open("DP-바닥 공사.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    for i in range(3,n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]
    print(dp)
    print(dp[n])