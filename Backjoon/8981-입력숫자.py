# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("8981-입력숫자-3.txt", "r")

input = sys.stdin.readline

N = int(input())
nl = list(map(int, input().split()))

answer = [-1] * N

now_index = 0
for i, e in enumerate(nl):
    answer[now_index] = e
    now_index = (now_index + e) % N
    while answer[now_index] != -1 and i != N-1:
        now_index = (now_index + 1) % N

answer_copied = answer[:]

answer_r = [-1] * N
count = 0
now_index = 0
value = answer_copied[now_index]
while count < N:
    while value == 0:
        now_index = (now_index+1)%N
        value = answer_copied[now_index]
    answer_r[count] = value
    count += 1
    answer_copied[now_index] = 0
    now_index = (value + now_index) % N
    value = answer_copied[now_index]

print(N)
print(*answer)
# if nl == answer_r:
#     print(*answer)
# else:
#     print(-1)