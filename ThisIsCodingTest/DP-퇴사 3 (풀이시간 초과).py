import sys

sys.stdin = open("DP-퇴사.txt", "r" ,encoding='utf-8')
input = sys.stdin.readline # 꼭 sys.stdin 밑에

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Times = [0]
    Prices = [0]
    for _ in range(N):
        t, p = map(int, input().split())
        Times.append(t)
        Prices.append(p)
    dp = [0] * (N+2)
    # print(Times)
    # print(Prices)
    for i in range(1,N+1):
        dp[i] = max(dp[i], dp[i - 1])
        if i+Times[i] <= N+1:
            dp[i+Times[i]] = max(dp[i+Times[i]],dp[i] + Prices[i])
    dp[N+1] = max(dp[N+1], dp[N])
    # print(dp)
    print(dp[N+1])