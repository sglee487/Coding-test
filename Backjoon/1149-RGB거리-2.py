import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("1149-RGB거리-5.txt", "r")

input = sys.stdin.readline

INF = 987654321

N = int(input())
rgbs = [list(map(int, input().split())) for _ in range(N)]

dp = [[INF] * 3 for _ in range(N)]
dp[0] = rgbs[0]
for r in range(1,N):
    for color in range(3):
        for other_color in range(3):
            if color == other_color: continue
            dp[r][color] = min(dp[r][color], rgbs[r][color] + dp[r-1][other_color])

print(min(dp[-1]))