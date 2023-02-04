# -*- coding: utf-8 -*-
from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2641-다각형그리기-1.txt", "r")

input = sys.stdin.readline

N = int(input())
nl = list(map(int, input().split()))
M = int(input())
ml = [list(map(int, input().split())) for _ in range(M)]

ad = {1: 1, 2: 0, 3: 3, 4: 2}
rv = {1: 3, 2:4, 3:1, 4:2}

nlr = [rv[a] for a in nl[::-1]]

candies = set()

Q = deque(nl)
candies.add(tuple(nl))

for _ in range(N):
    Q.append(Q.popleft())
    candies.add(tuple(Q))

Q = deque(nlr)
candies.add(tuple(nlr))

for _ in range(N):
    Q.append(Q.popleft())
    candies.add(tuple(Q))

al = []
for cl in ml:
    if tuple(cl) in candies:
        al.append(cl)

print(len(al))
for a in al:
    print(*a)
