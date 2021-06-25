import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("11727-2xn 타일링 2-3.txt", "r")

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
    exit()
if N == 2:
    print(3)
    exit()

dp = [0] * (N+1)
dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = (dp[i-2]*2 + dp[i-1]) % 10007
print(dp[N])