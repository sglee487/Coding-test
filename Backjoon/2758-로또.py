import sys
import math
sys.setrecursionlimit(10**9)

sys.stdin = open("2758-로또-1.txt", "r")

input = sys.stdin.readline


T = int(input())
for test_case in range(T):
    n, m = map(int, input().split())
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[0] = [0] * (m+1)
    dp[1] = list(range(m+1))
    for r in range(2, n+1):
        dp[r][0] = 0
    for r in range(2,n+1):
        for c in range(1, m+1):
            dp[r][c] = dp[r-1][c//2] + dp[r][c-1]
    print(*dp, sep='\n')
    print(dp[n][m])
    # 1,2,4,8,16,32,16,128,256,512
    # 1 2 4 8
    # 1.25 2.5 5 10
    # 1 2 5 10

    # 1 2 4 8
    # 1.25 2.5 5 11
    # 1 2 5 10
