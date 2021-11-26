# -*- coding: utf-8 -*-
import copy
import sys
from itertools import combinations
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2643-색종이 올려 놓기-1.txt", "r")

input = sys.stdin.readline

N = int(input())
nl = []
for _ in range(N):
    a, b = map(int, input().split())
    nl.append((min(a,b),max(a,b)))

nl.sort(key=lambda x:(x[0], x[1]))

def lis(nl):
    LIS = [1] * N
    C = [999999] * (N+1)
    C[0] = 0

    for i, e in enumerate(nl):
        c_index = bisect_right(C,e[1])
        C[c_index] = e[1]
        LIS[i] = c_index

    return max(LIS)

print(lis(nl))