import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("12865-평범한 배낭.txt", "r")

# input = sys.stdin.readline

N, K = map(int, input().split())
wl = [0]
vl = [0]
for _ in range(N):
    w, v = map(int, input().split())
    wl.append(w)
    vl.append(v)

dp = [[0] * (K+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, K+1):
        if c < wl[r]:
            dp[r][c] = dp[r-1][c]
        else:
            dp[r][c] = max(dp[r-1][c], dp[r-1][c-wl[r]] + vl[r])

print(dp[N][K])