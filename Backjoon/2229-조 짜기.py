# -*- coding: utf-8 -*-
from bisect import bisect_left
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2229-조 짜기-1.txt", "r")

input = sys.stdin.readline

N = int(input())
nl = list(map(int, input().split()))

print(N)
print(list(range(N)))
print(nl)

scores = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        scores[i][j] = max(nl[i:j+1]) - min(nl[i:j+1])

print(*scores, sep='\n')

