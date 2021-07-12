import sys
sys.setrecursionlimit(10**9)
from collections import deque

sys.stdin = open("16397-탈출-7.txt", "r")

input = sys.stdin.readline

def bnum(n):
    if n == 0:
        return 0
    n *= 2
    if n > 99999:
        return -1
    ja = 10**(len(str(n))-1)
    n -= ja
    return n

def bfs(Q, nums):
    global N, T, G
    while Q:
        n, d = Q.popleft()
        if G == n:
            return d
        if n+1 <= 99999 and nums[n+1] == -1 and d < T:
            nums[n + 1] = d + 1
            Q.append((n+1, d+1))
        bn = bnum(n)
        if bn != -1 and bn <= 99999 and nums[bn] == -1 and d < T:
            nums[bn] = d + 1
            Q.append((bn, d+1))

    return "ANG"

N, T, G = map(int, input().split())
nums = [-1] * (100000)
Q = deque()
Q.append((N,0))
nums[N] = 0
print(bfs(Q, nums))