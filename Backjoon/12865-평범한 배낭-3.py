import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("12865-평범한 배낭.txt", "r")

input = sys.stdin.readline

N, K = map(int, input().split())
wl = [0]
vl = [0]
for _ in range(N):
    w, v = map(int, input().split())
    wl.append(w)
    vl.append(v)

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(K+1):
        if j-wl[i] >= 0:
            dp[i][j] = max(dp[i-1][j-wl[i]] + vl[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]



# print(*dp, sep='\n')

print(dp[-1][-1])