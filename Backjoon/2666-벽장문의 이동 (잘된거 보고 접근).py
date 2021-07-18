import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("2666-벽장문의 이동-1.txt", "r")

input = sys.stdin.readline
# https://www.acmicpc.net/source/30937831
def dfs(a, b, step):
    global L, sequence
    if step == L:
        return 0
    if dp[step][a][b] != -1:
        return dp[step][a][b]
    target = sequence[step]
    ma = dfs(target, b, step+1) + abs(target-a)
    mb = dfs(a, target, step+1) + abs(target-b)
    dp[step][a][b] = min(ma, mb)
    return dp[step][a][b]

N = int(input())
closets = [1] * (N+1)
a, b = map(int, input().split())
closets[a] = 0
closets[b] = 0
L = int(input())
sequence = []
for _ in range(L):
    sequence.append(int(input()))
dp = [[[-1 for _ in range(N+1)] for _ in range(N+1)] for _ in range(L)]
answer = dfs(a, b, 0)
print(answer)