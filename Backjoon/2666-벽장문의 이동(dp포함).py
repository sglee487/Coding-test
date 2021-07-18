import sys

sys.setrecursionlimit(10**9)

sys.stdin = open("2666-벽장문의 이동-1.txt", "r")

def dfs(a, b, step):
    global L, targets, dp
    if step == L:
        return 0
    if dp[a][b][step] != -1:
        return dp[a][b][step]
    elif dp[b][a][step] != -1:
        return dp[b][a][step]
    target = targets[step]
    ra = dfs(a, target, step+1) + abs(target-b)
    rb = dfs(target, b, step+1) + abs(target-a)
    dp[a][b][step] = min(ra, rb)
    dp[b][a][step] = min(ra, rb)
    return dp[a][b][step]

input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
L = int(input())
dp = [[[-1 for _ in range(L+1)] for _ in range(N+1)] for _ in range(N+1)]
answer = 987654321
targets = []
for _ in range(L):
    targets.append(int(input().strip()))

print(dfs(a,b,0))