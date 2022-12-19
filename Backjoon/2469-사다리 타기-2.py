# -*- coding: utf-8 -*-
import copy
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2469-사다리 타기-2.txt", "r")

input = sys.stdin.readline

k = int(input())
n = int(input())
start = list(chr(ord('A')+i) for i in range(k))
goal = list(input().strip())

ladder = [input().strip() for _ in range(n)]

mid = int()
for i in range(len(ladder)):
    if ladder[i][0] == '?':
        mid = i
        break


def go_row(now, lad):
    c_now = copy.deepcopy(now)
    for i in range(k-1):
        if lad[i] == '-':
            c_now[i], c_now[i+1] = c_now[i+1], c_now[i]
    return c_now

for i in range(mid):
    start = go_row(start, ladder[i])

for i in range(n-1,mid,-1):
    goal = go_row(goal, ladder[i])

answer = ''

def dfs(lad):
    global answer
    if len(lad) > k-1:
        if goal == go_row(start, lad):
            answer = lad[:k-1]
            return True
        return False
    result = False
    result = result or dfs('*' + lad)
    result = result or dfs('-*' + lad)
    return result

if dfs(''):
    print(answer)
else:
    print('x'*(k-1))