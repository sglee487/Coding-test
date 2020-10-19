import sys

sys.stdin = open("DP-바닥 공사.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3,N+1):
        dp[i] = dp[i-1] + dp[i-2] * 2
    print(dp[N])