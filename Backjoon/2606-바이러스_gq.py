import sys
sys.setrecursionlimit(10**9)
from collections import deque


sys.stdin = open("2606-바이러스-1.txt", "r")

# input = sys.stdin.readline

N = int(input())
G = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(G):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

afl = [0] * (N+1)
afl[1] = 1

Q = deque()
Q.append(1)
while Q:
    now_af = Q.pop()
    for child in graph[now_af]:
        if not afl[child]:
            Q.append(child)
            afl[child] = 1

# print(afl)
print(sum(afl)-1)