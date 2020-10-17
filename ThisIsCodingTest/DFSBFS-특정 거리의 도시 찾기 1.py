# https://www.acmicpc.net/problem/18352
from collections import deque
import sys

# 밑은 백준용 읽기 코드
# import sys
# input = sys.stdin.readline

sys.stdin = open("DFSBFS-특정 거리의 도시 찾기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M, K, X = map(int, input().split())
    wl = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        wl[a].append(b)
    visited = [False] * (N+1)
    Q = deque()
    Q.append((X,0))
    result = []
    while Q:
        node, wn = Q.popleft()
        if visited[node]: continue
        else: visited[node] = True
        if wn == K:
            result.append(node)
            continue
        for cn in wl[node]:
            Q.append((cn,wn+1))
    if not result:
        print(-1)
    else:
        print(*result,sep='\n')