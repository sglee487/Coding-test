import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("16500-문자열 판별.txt", "r")

input = sys.stdin.readline


S = input().strip()
N = int(input())
al = [input().strip() for _ in range(N)]

dp = [-1] * 101

def dfs(index):
    global S, N, al
    if index == len(S):
        dp[index] = 1
        return 1
    if dp[index] != -1:
        return dp[index]
    dp[index] = 0
    for a in al:
        l = len(a)
        if index+l <= len(S) and S[index:index+l] == a:
            dp[index] = max(dp[index], dfs(index+l))
    return dp[index]

answer = dfs(0)
if answer == 1:
    print(1)
else:
    print(0)