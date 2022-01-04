# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2229-조 짜기-3.txt", "r")

input = sys.stdin.readline

N = int(input())
nl = list(map(int, input().split()))

print(N)
print(nl)
max_values = [[0] * N for _ in range(N)]
min_values = [[0] * N for _ in range(N)]
scores = [[0] * N for _ in range(N)]
for i in range(N):
    max_value = 0
    min_value = 1001
    for j in range(i,N):
        max_value = max(nl[j], max_value)
        min_value = min(nl[j], min_value)
        scores[i][j] = max_value - min_value
        max_values[i][j] = max_value
        min_values[i][j] = min_value

print('-'*10)
print(*scores, sep='\n')

dp = [-1] * (N+1)
def dfs(start, now):
    global N, scores
    if dp[start] != -1:
        return dp[start]
    dp[start] = 0
    value = 0
    print(start, N, now)
    if start == N:
        value = max(now, value)
    for l in range(N-start):
        value = max(value, dfs(start+l+1, now + scores[start][start+l]))
    dp[start] = value
    return value

dfs(0,0)

print(dp)