import sys

sys.stdin = open("DP-효율적인 화폐 구성2.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    dp = [10001] * (10001)
    dp[0] = 0
    coins = []
    for _ in range(N):
        coins.append(int(input()))
    for coin in coins:
        for i in range(coin,M+1):
            dp[i] = min(dp[i],dp[i-coin]+1)
        print(dp)