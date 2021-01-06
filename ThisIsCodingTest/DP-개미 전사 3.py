from collections import deque
import sys

# 밑은 백준용 읽기 코드
# import sys
# input = sys.stdin.readline

sys.stdin = open("DP-개미 전사.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    foods = list(map(int, input().split()))
    dp = [0] * (N)
    dp[0] = foods[0]
    dp[1] = max(foods[0], foods[1])
    for i in range(2,N):
        dp[i] = max(dp[i-1],dp[i-2]+foods[i])
    print(dp)
    print(dp[N-1])