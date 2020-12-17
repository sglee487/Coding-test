import sys
import heapq

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
sys.stdin = open("최단경로-화성 탐사.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    distances = [[INF] * N for _ in range(N)]
    distances[0][0] = Map[0][0]
    visited = [[False] * N for _ in range(N)]
    hq = []
    heapq.heappush(hq,(abs(Map[0][0] - Map[0][1]),0,1,Map[0][0]))
    heapq.heappush(hq,(abs(Map[0][0] - Map[1][0]),1,0,Map[0][0]))
    visited[0][0] = True
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    result = int()
    while heapq:
        d, r, c, sm = heapq.heappop(hq)
        if r == N-1 and c == N-1:
            result = sm
            break
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                visited[nr][nc] = True
                heapq.heappush(hq,(abs(Map[nr][nc]-Map[r][c]),nr,nc,sm+Map[r][c]))
    print(result)