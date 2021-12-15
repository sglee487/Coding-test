# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("10835-카드게임-3.txt", "r")

input = sys.stdin.readline

N = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

dp = [[-1] * N for _ in range(N)]

def solve(left_i,right_i):
    global al,bl,dp,N
    if left_i >= N or right_i >= N:
        return 0
    if dp[left_i][right_i] != -1:
        return dp[left_i][right_i]
    dp[left_i][right_i] = 0
    result = max(solve(left_i+1, right_i), solve(left_i+1, right_i+1))
    if bl[right_i] < al[left_i]:
        result = solve(left_i, right_i+1) + bl[right_i]
    dp[left_i][right_i] = result
    return result

print(solve(0,0))
