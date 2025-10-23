import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("2666-벽장문의 이동-1.txt", "r")

input = sys.stdin.readline

INF = 987654321

N = int(input())
a, b = map(int, input().split())
T = int(input())
ol = list(int(input()) for _ in range(T))

dp = [[[-1 for _ in range(N+1)] for _ in range(N+1)] for _ in range(T)]

def dfs(step, now_a, now_b):
    global ol

    if step == T:
        return 0

    if dp[step][now_a][now_b] != -1:
        return dp[step][now_a][now_b]

    target = ol[step]

    result_a = dfs(step+1, target, now_b) + abs(now_a - target)
    result_b = dfs(step+1, now_a, target) + abs(now_b - target)

    result = min(result_a, result_b)

    dp[step][now_a][now_b] = result

    return result

print(dfs(0, a, b))
