import sys
import heapq

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
sys.stdin = open("최단경로-화성 탐사.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    distances = [[INF] * N for _ in range(N)]
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    hq = []
    heapq.heappush(hq,(Map[0][0],0,0))
    while hq:
        dist, x, y = heapq.heappop(hq)
        if distances[x][y] < dist: continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not(0<=nx<N and 0<=ny<N): continue
            cost = dist + Map[nx][ny]
            if cost < distances[nx][ny]:
                distances[nx][ny] = cost
                heapq.heappush(hq,(cost,nx,ny))
    print(*distances,sep='\n')