from collections import deque
import sys

sys.stdin = open("DFSBFS-인구 이동.txt", "r")
# https://github.com/ndb796/python-for-coding-test/blob/master/13/7.py
# https://www.acmicpc.net/source/23286182

def bfs(r,c):
    # 위 오 아래 왼
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    unions = [(r,c)]
    UQ = deque([(r,c)])
    peoples = Maps[r][c]
    visited[r][c] = 1
    while UQ:
        r, c = UQ.popleft()
        for i in range(4):
            nr, nc = r+dy[i], c+dx[i]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                if L<=abs(Maps[r][c]-Maps[nr][nc])<=R:
                    visited[nr][nc] = 1
                    peoples += Maps[nr][nc]
                    UQ.append((nr,nc))
                    unions.append((nr,nc))
    if len(unions) > 1:
        for r, c in unions:
            Maps[r][c] = peoples // len(unions)
            Q.append((r,c))
        return True
    else:
        return False


T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, L, R = map(int, input().split())
    Maps = [list(map(int, input().split())) for _ in range(N)]
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    Q = deque()
    for r in range(N):
        for c in range(N):
            Q.append((r,c))
    total_count = 0
    while True:
        visited = [[0] * N for _ in range(N)]
        changed = False
        Qsize = len(Q)
        for _ in range(Qsize):
            r, c = Q.popleft()
            if visited[r][c]: continue
            if bfs(r,c): changed = True
        if not changed: break
        else: total_count += 1

    print(total_count)