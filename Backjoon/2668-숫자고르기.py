# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2668-숫자고르기-1.txt", "r")

input = sys.stdin.readline

N = int(input())

graph = [0] * (N+1)

for i in range(N):
    graph[i+1] = int(input())

result_set = set()

def is_cycle(i):
    visited = [False] * (N+1)
    visited[i] = True
    nxt_i = graph[i]
    while True:
        if nxt_i == i:
            return True
        else:
            if visited[nxt_i]:
                return False
            else:
                visited[nxt_i] = True
                nxt_i = graph[nxt_i]

    return False

for i in range(1,N+1):
    if is_cycle(i):
        result_set.add(i)

print(len(result_set))
print(*sorted(list(result_set)), sep='\n')