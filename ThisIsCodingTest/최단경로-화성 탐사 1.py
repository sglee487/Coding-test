import sys
import heapq
from collections import deque

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
sys.stdin = open("최단경로-화성 탐사.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    distance = [[INF] * N for _ in range(N)]
    Matrix = []
    for _ in range(N):
        Matrix.append(list(map(int, input().split())))
    print(*Matrix,sep='\n')
    # 위 오른쪽 아래 왼쪽
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    Q = [(Matrix[0][0],0,0)]
    Q.append((Matrix[0][0],0,0))
    while Q:
        dist, r, c = heapq.heappop(Q)
        if distance[r][c] < dist:
            continue
        for i in range(4):
            nr = r + dy[i]
            nc = c + dx[i]
            if not(0<=nr<N and 0<=nc<N): continue
            cost = dist + Matrix[nr][nc]
            if cost < distance[nr][nc]:
                distance[nr][nc] = cost
                heapq.heappush(Q,(dist+Matrix[nr][nc],nr,nc))

    print(*distance,sep='\n')