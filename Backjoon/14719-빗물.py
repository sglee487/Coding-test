from collections import deque
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("14719-빗물-1.txt", "r")

input = sys.stdin.readline

H, W = map(int, input().split())
heights = list(map(int, input().split()))

def water_here(now_w):
    left_max, right_max = 0, 0
    for w in range(now_w,-1,-1):
        left_max = max(left_max,heights[w])
    for w in range(now_w,W):
        right_max = max(right_max,heights[w])

    return min(left_max,right_max) - heights[now_w]

total = 0
for w in range(1,W-1):
    total += water_here(w)
print(total)