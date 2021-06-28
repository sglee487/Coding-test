import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("9465-스티커.txt", "r")

input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    Stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = Stickers[0][0]
    dp[1][0] = Stickers[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1] + Stickers[0][i])
        dp[1][i] = max(dp[1][i-1], dp[0][i-1] + Stickers[1][i])
    print(max(dp[0][-1], dp[1][-1]))