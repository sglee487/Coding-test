# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2229-조 짜기-3.txt", "r")

input = sys.stdin.readline

N = int(input())
nl = list(map(int, input().split()))

# print(N)
# print(nl)

dp = [0] * (N+1)
for i in range(1, N):
    min_value = 10001
    max_value = 0
    for j in range(i,-1,-1):
        min_value = min(min_value, nl[j])
        max_value = max(max_value, nl[j])
        dp[i+1] = max(dp[i+1], max_value - min_value + dp[j-1+1])

print(dp[N])