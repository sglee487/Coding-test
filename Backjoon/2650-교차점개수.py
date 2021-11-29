# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2650-교차점개수-1.txt", "r")

input = sys.stdin.readline

N = int(input())
M = N//2
ml = []
for _ in range(M):
    a, b, c, d = map(int, input().split())
    if a == 1:
        ab = b
    elif a == 2:
        ab = 2*50 + (50-b)
    elif a == 3:
        ab = 3*50 + (50-b)
    elif a == 4:
        ab = 1*50 + b
    if c == 1:
        cd = d
    elif c == 2:
        cd = 2*50 + (50-d)
    elif c == 3:
        cd = 3*50 + (50-d)
    elif c == 4:
        cd = 1*50 + d
    ml.append((min(ab,cd), max(ab,cd)))

ml.sort()

total_count = 0
max_count = 0

for i in range(M):
    i_count = 0
    for j in range(M):
        if i == j: continue
        if (ml[j][0] < ml[i][0] and ml[i][0] < ml[j][1] < ml[i][1]) \
            or (ml[i][0] < ml[j][0] < ml[i][1] and ml[j][1] > ml[i][1]):
            i_count += 1
    max_count = max(max_count, i_count)
    total_count += i_count

print(total_count//2)
print(max_count)