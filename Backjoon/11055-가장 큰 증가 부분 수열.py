from bisect import bisect_left
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("11055-가장 큰 증가 부분 수열.txt", "r")

input = sys.stdin.readline

N = int(input())
Al = list(map(int, input().split()))
M = len(Al)

dp = Al[:]

for i in range(M):
    for j in range(i):
        if Al[i] > Al[j]:
            dp[i] = max(dp[i], dp[j] + Al[i])

print(max(dp))