# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2302-극장 좌석-1.txt", "r")

input = sys.stdin.readline

N = int(input())
M = int(input())
ml = [int(input()) for _ in range(M)]

nl = [1,1,2,3]
for i in range(4, 41):
    nl.append(nl[i-1] + nl[i-2])

result = 1
nml = [0] + ml + [N+1]
# print(nl)
# print(nml)
for i in range(len(nml)-1):
    result *= nl[(nml[i+1] - nml[i])-1]
print(result)