# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2302-극장 좌석-1.txt", "r")

input = sys.stdin.readline

N = int(input())
M = int(input())
cl = []
for _ in range(M):
    cl.append(int(input()))
cl.append(N+1)
counts = [1] * (N+2)
counts[1] = 1
counts[2] = 2
for i in range(3, N+1):
    counts[i] = counts[i-1] + counts[i-2]

# print(counts)

answer = 1
now = 1
for c in cl:
    answer *= counts[(c-now)]
    now = c+1

print(answer)