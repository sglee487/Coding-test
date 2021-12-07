# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2559-수열-2.txt", "r")

input = sys.stdin.readline

N, K = map(int, input().split())
nl = list(map(int, input().split()))

result = -99999999
now_sum = sum(nl[:K])
result = max(result, now_sum)
for i in range(N-K):
    now_sum -= nl[i]
    now_sum += nl[i+K]
    result = max(result, now_sum)
print(result)