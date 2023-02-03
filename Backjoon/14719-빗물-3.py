from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("14719-빗물-2.txt", "r")

input = sys.stdin.readline

H, W = map(int, input().split())
hl = list(map(int, input().split()))
hl.insert(0,0)
hl.append(0)
N = len(hl)

def cal_height(w):
    left_top = max(hl[:w])
    right_top = max(hl[w+1:])
    return max(0, min(left_top, right_top) - hl[w])

answer = 0
for i in range(1, N-1):
    answer += cal_height(i)

print(answer)