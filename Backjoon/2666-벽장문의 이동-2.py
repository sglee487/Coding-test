import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("2666-벽장문의 이동-1.txt", "r")

input = sys.stdin.readline

def dfs_dp(a, b, step):
    global dp, result, S, sl
    if step == S:
        return 0
    if dp[step][a][b] != -1: return dp[step][a][b]
    dp[step][a][b] = min(
        abs(sl[step]-a) + dfs_dp(sl[step],b,step+1),
        abs(sl[step] - b) + dfs_dp(a, sl[step], step + 1)
    )

    return dp[step][a][b]

L = int(input())
a, b = map(int, input().split())
S = int(input())
sl = [int(input()) for _ in range(S)]

dp = [[[-1 for _ in range(L+1)] for _ in range(L+1)] for _ in range(S+1)]

result = dfs_dp(a,b,0)
print(result)