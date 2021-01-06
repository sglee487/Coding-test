import sys

sys.stdin = open("DP-개미 전사.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nlist = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = nlist[0]
    dp[1] = max(nlist[0],nlist[1])
    for i in range(2,N):
        dp[i] = max(dp[i-1],nlist[i] + dp[i-2])
    print(dp[N-1])