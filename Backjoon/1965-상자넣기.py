# -*- coding: utf-8 -*-
from bisect import bisect_left
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("1965-상자넣기-2.txt", "r")

input = sys.stdin.readline

N = int(input())
boxes = list(map(int, input().split()))

def LIS(boxes):
    global N
    lis = [1] * (N+1)
    C = [1001] * (N+1)
    C[0] = 0

    for i in range(N):
        c_index = bisect_left(C, boxes[i])
        lis[i] = c_index
        C[c_index] = boxes[i]

    return max(lis)

print(LIS(boxes))