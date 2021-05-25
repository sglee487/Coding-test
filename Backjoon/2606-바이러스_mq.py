import sys
sys.setrecursionlimit(10**9)
from collections import deque


sys.stdin = open("2606-바이러스-1.txt", "r")

# input = sys.stdin.readline

N = int(input())
G = int(input())
mat = [[0] * (N+1) for _ in range(N+1)]
for _ in range(G):
    a, b = map(int, input().split())
    mat[a][b] = 1
    mat[b][a] = 1

afl = [0] * (N+1)
afl[1] = 1

Q = deque()
Q.append(1)
while Q:
    now = Q.pop()
    for i in range(1, N+1):
        if mat[now][i] == 1:
            if afl[i] == 0:
                afl[i] = 1
                Q.append(i)

# print(afl)
print(sum(afl)-1)