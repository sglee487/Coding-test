import sys

sys.stdin = open("11726-2xn 타일링-2.txt", "r")

input = sys.stdin.readline

n = int(input())
dp = [0] * ((n+1) if (n+1) >= 2+1 else 2+1)
dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = dp[i-2] + dp[i-1]

# print(dp)
print(dp[n]%10007)