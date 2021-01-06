import sys

sys.stdin = open("DP-효율적인 화폐 구성.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    coins = []
    for _ in range(N):
        coins.append(int(input()))
    dp = [9999999] * (10001)
    dp[0] = 0
    for coin in coins:
        dp[coin] = 1
    for i in range(min(coins),M+1):
        for coin in coins:
            dp[i] = min(dp[i],dp[i-coin]+1)
    print(dp)
    if dp[M] == 9999999:
        print(-1)
    else:
        print(dp[M])
