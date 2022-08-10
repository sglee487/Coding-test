import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("12865-평범한 배낭.txt", "r")

input = sys.stdin.readline

N, K = map(int, input().split())
wl, vl = [[]], [[]]
for _ in range(N):
    temp_input = list(map(int, input().split()))
    wl.append(temp_input[0])
    vl.append(temp_input[1])

dp = [[0] * (K+1) for _ in range(N+1)]
for r in range(1,N+1):
    for k in range(1,K+1):
        if k < wl[r]:
            dp[r][k] = dp[r-1][k]
        else:
            dp[r][k] = max(dp[r-1][k], dp[r-1][k-wl[r]] + vl[r])

# print(*dp, sep='\n')
print(dp[N][K])