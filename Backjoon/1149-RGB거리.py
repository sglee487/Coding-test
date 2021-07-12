from collections import deque

import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("1149-RGB거리-1.txt", "r")

input = sys.stdin.readline

N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]
dp = [[987654321] * 3 for _ in range(N)]
dp[0] = RGB[0]
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1] + RGB[i][0], dp[i-1][2] + RGB[i][0])
    dp[i][1] = min(dp[i-1][0] + RGB[i][1], dp[i-1][2] + RGB[i][1])
    dp[i][2] = min(dp[i-1][0] + RGB[i][2], dp[i-1][1] + RGB[i][2])
print(min(dp[-1]))