# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2294-동전 2.txt", "r")

input = sys.stdin.readline
ccccccc

n, k = map(int, input().split())
nl = [int(input()) for _ in range(n)]

dp = [99999] * 999999
dp[0] = 0

for i in range(k):
    for n in nl:
        dp[i+n] = min(dp[i+n], dp[i]+1)

print(dp[k] if dp[k] != 99999 else -1)