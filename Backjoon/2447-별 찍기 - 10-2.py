import sys
import math
sys.setrecursionlimit(10**9)

sys.stdin = open("2447-별 찍기 - 10.txt", "r")

input = sys.stdin.readline

N = int(input())

dp = [[' '] * N for _ in range(N)]


def star(y,x,n):
    if n == 1:
        dp[y][x] = '*'
        return

    m = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: continue
            star(i * m + y, j * m + x, m)


star(0,0,N)

for d in dp:
    print(''.join(d))