import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("11057-오르막 수-3.txt", "r")

# input = sys.stdin.readline

N = int(input())

dp = [[-1] * 11 for _ in range(N+1)]
if N == 1:
    print(10)
elif N == 2:
    print(55)
else:
    dp[1] = [1,1,1,1,1,1,1,1,10]
    dp[2] = [10,9,8,7,6,5,4,3,2,1,55]
    for i in range(3,N+1):
        acnum = dp[i-1][10]
        for j in range(11):
            dp[i][j] = acnum
            acnum -= dp[i-1][j]
        dp[i][10] = sum(dp[i])

    print(dp[N][10])