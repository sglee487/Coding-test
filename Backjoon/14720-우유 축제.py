import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("14720-우유 축제-1.txt", "r")

input = sys.stdin.readline

N = int(input())
village = list(map(int, input().split()))
dp = [[0] * 3 for _ in range(N)]
dp[0][0] = 1 if village[0] == 0 else 0

for i in range(1,N):
    if village[i] == 0:
        dp[i][0] = max(dp[i-1][0], dp[i-1][2]+1)
    else:
        dp[i][0] = dp[i-1][0]
    if dp[i-1][0] > dp[i-1][2] and village[i] == 1:
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]+1)
    else:
        dp[i][1] = dp[i-1][1]
    if dp[i-1][1] > dp[i-1][0] and village[i] == 2:
        dp[i][2] = max(dp[i-1][2], dp[i-1][1]+1)
    else:
        dp[i][2] = dp[i-1][2]

print(max(dp[N-1]))
# print(village)
# print(*dp, sep='\n')