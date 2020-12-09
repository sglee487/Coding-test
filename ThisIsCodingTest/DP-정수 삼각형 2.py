import sys

sys.stdin = open("DP-정수 삼각형.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    triarr = [[0] * (N+1) for _ in range(N)]
    for i in range(N):
        for j, e in enumerate(map(int, input().split()),1):
            triarr[i][j] = e
    # print(*triarr,sep='\n')
    dp = [[0] * (N+1) for _ in range(N)]
    dp[0][1] = triarr[0][1]
    for i in range(1,N):
        for j in range(1,i+2):
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triarr[i][j]
    # print(*dp, sep='\n')
    print(max(dp[N-1]))