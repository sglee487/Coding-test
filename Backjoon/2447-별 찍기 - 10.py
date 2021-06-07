import sys
import math
sys.setrecursionlimit(10**9)

sys.stdin = open("2447-별 찍기 - 10.txt", "r")

input = sys.stdin.readline

N = int(input())

dp = [[' '] * N for _ in range(N)]

def drawstar(step, r, c, dp):
    if step == 1:
        dp[r][c:c+3] = ['*' for _ in range(3)]
        dp[r+1][c:c+3] = ['*', ' ', '*']
        dp[r+2][c:c+3] = ['*' for _ in range(3)]
    else:
        drawstar(step-1, r, c, dp)
        drawstar(step-1, r, c+3**(step-1), dp)
        drawstar(step-1, r, c+2*(3**(step-1)),dp)

        drawstar(step-1, r+3**(step-1), c,dp)
        drawstar(step-1, r+3**(step-1), c+2*(3**(step-1)),dp)

        drawstar(step-1, r+(2*(3**(step-1))), c,dp)
        drawstar(step-1, r+(2*(3**(step-1))), c+3**(step-1),dp)
        drawstar(step-1, r+(2*(3**(step-1))), c+2*(3**(step-1)),dp)



step = round(math.log(N, 3))
drawstar(step, 0, 0, dp)

for r in dp:
    print(''.join(r))