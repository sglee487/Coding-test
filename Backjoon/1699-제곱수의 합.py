import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("1699-제곱수의 합-2.txt", "r")

input = sys.stdin.readline

N = int(input())

def is_square(n):
    return int(n**0.5)**2 == n

dp = [999999] * (N+1)
dp[0] = 0
square = 1
sql = []
for i in range(1, N+1):
    if is_square(i):
        square = i
        sql.append(i)
        dp[i] = 1
    else:
        for sq in sql:
            if i-sq < sq: break
            dp[i] = min(dp[i], dp[i-sq] + dp[sq])

# [0,1,2,3,1,2,3,4,2,1,2,3,3,2]

# print(dp)
print(dp[N])