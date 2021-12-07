# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("10164-격자상의 경로-1.txt", "r")

input = sys.stdin.readline

N, M, K = map(int, input().split())

goal = ((K-1) // M, (K-1) % M)

# 오 아래
dy = [0, 1]
dx = [1, 0]


def find_paths(r, c, rn, cn, dp):
    if dp[r][c] != -1:
        return dp[r][c]
    if (r, c) == (rn - 1, cn - 1):
        dp[r][c] = 1
        return dp[r][c]
    count = 0
    for i in range(2):
        nr, nc = r + dy[i], c + dx[i]
        if 0 <= nr < rn and 0 <= nc < cn:
            count += find_paths(nr, nc, rn, cn, dp)
    dp[r][c] = count

    return dp[r][c]


def calcul_paths(start, goal):
    rn = goal[0] - start[0] + 1
    cn = goal[1] - start[1] + 1
    dp = [[-1] * cn for _ in range(rn)]
    find_paths(0, 0, rn, cn, dp)
    return find_paths(0, 0, rn, cn, dp)


if K:
    a = calcul_paths((0, 0), goal)
    b = calcul_paths(goal, (N - 1, M - 1))
    print(a * b)
else:
    print(calcul_paths((0, 0), (N - 1, M - 1)))
