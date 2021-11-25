# -*- coding: utf-8 -*-
import copy
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2116-주사위 쌓기-1.txt", "r")

input = sys.stdin.readline

N = int(input())
nl = [list(map(int, input().split())) for _ in range(N)]

# print(*nl, sep='\n')

opposite = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

def max_num(dice, upper_i):
    val = 0
    for i in range(6):
        if i == upper_i or i == opposite[upper_i]: continue
        val = max(val, dice[i])
    return val

def one_upper(i):
    total = 0
    now = 0
    while True:
        total += max_num(nl[now], i)
        if now == N-1:
            return total
        ceilng_bottom_num = nl[now][i]
        nxt_upper_i = opposite[nl[now+1].index(ceilng_bottom_num)]
        i = nxt_upper_i
        now += 1

    return total

def start():
    max_value = 0
    for i in range(6):
        max_value = max(max_value, one_upper(i))
    return max_value

print(start())