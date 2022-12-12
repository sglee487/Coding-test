# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2650-교차점개수-1.txt", "r")

input = sys.stdin.readline

N = int(input())
nd = {1:0, 4:1,2:2,3:3}
dots = []
for _ in range(N//2):
    a1, a2, b1, b2 = map(int, input().split())
    if a1 == 1 or a1 == 4:
        s = nd[a1]*51 + a2
    else:
        s = nd[a1]*51 + 51 - a2
    if b1 == 1 or b1 == 4:
        e = nd[b1]*51 + b2
    else:
        e = nd[b1]*51 + 51 - b2
    dots.append((min(s,e),max(s,e)))

dots.sort(key=lambda x:(x[0],x[1]))
# print(dots)
answer1 = 0
crosses = [0] * (N//2)
for i in range(N//2):
    a, b = dots[i]
    for j in range(i+1, N//2):
        c, d = dots[j]
        if b > c and b < d:
            # print(a,b,c,d)
            answer1 += 1
            crosses[i] += 1
            crosses[j] += 1

print(answer1)
print(max(crosses))