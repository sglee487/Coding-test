import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("2616-소형기관차-1.txt", "r")

input = sys.stdin.readline

N = int(input())
nl = list(map(int, input().split()))
L = int(input())

sl = [0] * (N+1)
s = 0
for i in range(N):
    s += nl[i]
    sl[i+1] = s

dp = [[0] * (N+1) for _ in range(4)]

for r in range(1,4):
    for c in range(r*L,N+1):
        dp[r][c] = max(dp[r][c-1], sl[c] - sl[c-L] + dp[r-1][c-L])

print(dp[3][N])