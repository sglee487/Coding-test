import sys
import heapq

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
sys.stdin = open("최단경로-화성 탐사.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    DMap = [[INF] * N for _ in range(N)]
    hq = [(Map[0][0],(0,0))]
    DMap[0][0] = Map[0][0]
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    result = INF
    # print(*Map, sep='\n')
    while hq:
        dist, (r,c) = heapq.heappop(hq)
        if dist < DMap[r][c]:
            DMap[r][c] = dist
        if (r,c) == (N-1,N-1):
            result = dist
            break
        for i in range(4):
            nr, nc = r+dy[i],c+dx[i]
            if not (0<=nr<N and 0<=nc<N): continue
            if DMap[nr][nc] < dist + Map[nr][nc]: continue
            heapq.heappush(hq,(dist+Map[nr][nc],(nr,nc)))
        # print(hq)
        # print(*DMap,sep='\n')
    print(result)