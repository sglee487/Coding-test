from collections import deque
import sys

# 밑은 백준용 읽기 코드
# import sys
# input = sys.stdin.readline

sys.stdin = open("DP-1로 만들기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    trylist = [0] * (n+1)
    for i in range(2, n+1):
        trylist[i] = trylist[i-1] + 1
        if i % 2 == 0:
            trylist[i] = min(trylist[i],trylist[i//2] + 1)
        if i % 3 == 0:
            trylist[i] = min(trylist[i],trylist[i//3] + 1)
        if i % 5 == 0:
            trylist[i] = min(trylist[i],trylist[i//5] + 1)
    print(trylist)