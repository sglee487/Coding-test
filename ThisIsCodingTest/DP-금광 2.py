import sys

sys.stdin = open("DP-금광.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nmlist = list(map(int, input().split()))
    matrix = [[0] * M for _ in range(N+2)]
    for i in range(N):
        for j in range(M):
            matrix[i+1][j] = nmlist[(i*M)+j]
    # print(*matrix,sep='\n')
    dp = [[0] * M for _ in range(N+2)]
    for i in range(N):
        dp[i][0] = matrix[i][0]
    maxvalue = 0
    for j in range(1,M):
        for i in range(1,N+1):
            dp[i][j] = max(dp[i][j],matrix[i][j] + dp[i-1][j-1],matrix[i][j] + dp[i][j-1],matrix[i][j] + dp[i+1][j-1])
            maxvalue = max(maxvalue,dp[i][j])
    # print(*dp, sep='\n')
    print(maxvalue)