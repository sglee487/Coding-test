import sys

sys.stdin = open("DP-퇴사.txt", "r",encoding='utf-8')
input = sys.stdin.readline # 꼭 sys.stdin 밑에
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    T = []
    P = []
    for _ in range(N):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)
    dp = [0] * 1006
    for n in range(N):
        dp[T[n]+n] = max(dp[T[n]+n],dp[n]+P[n])
        dp[n+1] = max(dp[n+1],dp[n])
    # print(dp)
    # print(dp[:N+1])
    print(dp[N])