import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2294-동전 2-2.txt", "r")

input = sys.stdin.readline

n, k = map(int, input().split())
cl = []
for _ in range(n):
    cl.append(int(input()))

dp = [99999] * (110001)
dp[0] = 0
for i in range(k+1):
    for c in cl:
        dp[i+c] = min(dp[i+c], dp[i] + 1)

if dp[k] == 99999:
    print(-1)
else:
    print(dp[k])