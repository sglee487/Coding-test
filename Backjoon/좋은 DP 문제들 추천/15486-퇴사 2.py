import sys

sys.stdin = open("15486-퇴사 2-3.txt", "r")

input = sys.stdin.readline

N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
T += [0]
P += [0]
dp = [0] * (N+2)
for i, (t,p) in enumerate(zip(T,P),1):
    dp[i] = max(dp[i], dp[i - 1])
    if i + t <= N+1:
        dp[i + t] = max(dp[i+t], dp[i] + p)

print(dp[N+1])