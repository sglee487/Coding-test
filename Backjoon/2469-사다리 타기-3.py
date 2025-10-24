# -*- coding: utf-8 -*-
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

# print(k)
# print(n)
# print(start)
# print(goal)
# print(ladder)

new_start = start[::]

for lad in ladder:
    if lad[0] == '?':
        break

    for i, l in enumerate(lad):
        if l == '-':
            new_start[i], new_start[i+1] = new_start[i+1], new_start[i]

new_goal = goal[::]

for lad in ladder[::-1]:
    if lad[0] == '?':
        break

    for i, l in enumerate(lad):
        if l == '-':
            new_goal[i], new_goal[i+1] = new_goal[i+1], new_goal[i]

# print(new_start)
# print(new_goal)

result = ['*'] * (k-1)

can_matching = True
skip = False

# print(result)

for i in range(k):
    if skip:
        skip = False
        continue
    if new_start[i] != new_goal[i]:
        if new_start[i+1] != new_goal[i]:
            can_matching = False
            break
        else:
            skip = True
            result[i] = '-'

if can_matching:
    print(''.join(result))
else:
    print('x' * (k-1))