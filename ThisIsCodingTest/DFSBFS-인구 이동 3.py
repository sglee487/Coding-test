from collections import deque
import sys

def bfs(r,c,unionnum):
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    unionmap[r][c] = unionnum
    Q = deque()
    Q.append((r,c))
    unions = [(r,c)]
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r+dy[i], c+dx[i]
            if not(0<=nr<N and 0<=nc<N): continue
            if unionmap[nr][nc] == -1 and L<=abs(Map[nr][nc]-Map[r][c])<=R:
                unionmap[nr][nc] = unionnum
                Q.append((nr,nc))
                unions.append((nr,nc))
    return unions

sys.stdin = open("DFSBFS-인구 이동.txt", "r")
T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, L, R = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(N)]
    # print(*Map,sep='\n')
    itercount = 0
    while True:
        unionmap = [[-1] * N for _ in range(N)]
        unionnum = 0
        unionstotal = []
        for r in range(N):
            for c in range(N):
                if unionmap[r][c] == -1:
                    unionstotal.append(bfs(r,c,unionnum))
                    unionnum += 1
        for union in unionstotal:
            totalpeople = 0
            for r, c in union:
                totalpeople += Map[r][c]
            ulen = len(union)
            for r, c in union:
                Map[r][c] = totalpeople // ulen
        if unionnum == N*N:
            break
        else:
            itercount += 1
        # print(*unionmap,sep='\n')
        # print(*Map,sep='\n')
    print(itercount)