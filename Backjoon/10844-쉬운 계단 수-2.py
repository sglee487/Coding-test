# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("10844-쉬운 계단 수.txt", "r")

input = sys.stdin.readline

N = int(input())

dp = [[0] * 10 for _ in range(N+1)]
for i in range(1,10):
    dp[1][i] = 1

for r in range(2,N+1):
    for c in range(10):
        if c >= 1:
            dp[r][c] += dp[r-1][c-1]
        if c+1 < 10:
            dp[r][c] += dp[r - 1][c + 1]

answer = 0
for c in range(10):
    answer += dp[N][c]
print(answer%1000000000)