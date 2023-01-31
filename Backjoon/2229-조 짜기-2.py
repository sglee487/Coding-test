# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2229-조 짜기-1.txt", "r")

input = sys.stdin.readline

N = int(input())
nl = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(N):
    min_value = 10000
    max_value = 0
    for j in range(i,-1,-1):
        min_value = min(nl[j], min_value)
        max_value = max(nl[j], max_value)
        dp[i+1] = max(dp[i+1], max_value - min_value + dp[j])

print(dp[N])
