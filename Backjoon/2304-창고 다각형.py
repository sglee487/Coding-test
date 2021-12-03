# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2304-창고 다각형-1.txt", "r")

input = sys.stdin.readline

N = int(input())
lhl = [tuple(map(int, input().split())) for _ in range(N)]
lhl.sort(key=lambda x: (x[0]))
lhl.insert(0,(0,0))
lhl.append((1001,0))
max_h_i = lhl.index(max(lhl, key=lambda x: (x[1])))

area = 0

left_i = 0
for i in range(1, max_h_i+1):
    if lhl[i][1] >= lhl[left_i][1]:
        area += ((lhl[i][0] - lhl[left_i][0]) * lhl[left_i][1])
        left_i = i

right_i = N+1
for i in range(N+1,max_h_i-1,-1):
    if lhl[i][1] >= lhl[right_i][1]:
        area += ((lhl[right_i][0] - lhl[i][0]) * lhl[right_i][1])
        right_i = i

area += lhl[max_h_i][1]

print(area)