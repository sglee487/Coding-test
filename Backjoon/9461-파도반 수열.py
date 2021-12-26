# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("9461-파도반 수열-1.txt", "r")

input = sys.stdin.readline

dp = [0] * (100 + 1)

dp[1:12] = [1,1,1,2,2,3,4,5,7,9,12]

for i in range(12,101):
    dp[i] = dp[i-1] + dp[i-5]

Test_case = int(input())

for _ in range(Test_case):
    N = int(input())
    print(dp[N])