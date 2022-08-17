import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("11055-가장 큰 증가 부분 수열.txt", "r")

# input = sys.stdin.readline

N = int(input())
al = list(map(int, input().split()))

if N == 1:
    print(al[0])
    exit()

dp = [0] * N
dp[0] = al[0]
for i in range(1,N):
    dp[i] = al[i]
    for j in range(i):
        if al[i] > al[j]:
            dp[i] = max(dp[i], dp[j] + al[i])

print(max(dp))