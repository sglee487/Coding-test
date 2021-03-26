import sys

sys.stdin = open("9095-1, 2, 3 더하기-1.txt", "r")

input = sys.stdin.readline

T = int(input())
for test_case in range(T):
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    n = int(input())
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])