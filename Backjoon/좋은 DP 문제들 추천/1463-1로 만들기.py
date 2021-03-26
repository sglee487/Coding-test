import sys

sys.stdin = open("1463-1로 만들기-2.txt", "r")

input = sys.stdin.readline

N = int(input())
INF = 10**7
dp = [INF] * ((10**7)+1)
print(len(dp))
now = 1
dp[now] = 0
while now < N:
    dp[now*3] = min(dp[now]+1,dp[now*3])
    dp[now*2] = min(dp[now]+1,dp[now*2])
    dp[now+1] = min(dp[now]+1,dp[now+1])
    now += 1
print(dp[N])
print(list(range(N+1)))
print(dp[:N+1])