from collections import deque
import sys

sys.stdin = open("DFSBFS-인구 이동2.txt", "r")
# https://github.com/ndb796/python-for-coding-test/blob/master/13/7.py

T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, L, R = map(int, input().split())
    Maps = [list(map(int, input().split())) for _ in range(N)]
    # print(*Maps,sep='\n')
    # print()
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    total_count = 0
    while True:
        count = 0
        UnionMaps = [[-1] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if UnionMaps[r][c] == -1:
                    Q = deque()
                    unions = []
                    count += 1
                    Q.append((r, c))
                    UnionMaps[r][c] = count
                    peopletotal = Maps[r][c]
                    unions.append((r, c))
                    while Q:
                        qr, qc = Q.popleft()
                        for i in range(4):
                            nr, nc = qr+dy[i],qc+dx[i]
                            if 0<=nr<N and 0<=nc<N and UnionMaps[nr][nc] == -1:
                                if L<=abs(Maps[qr][qc]-Maps[nr][nc])<=R:
                                    Q.append((nr,nc))
                                    UnionMaps[nr][nc] = count
                                    peopletotal += Maps[nr][nc]
                                    unions.append((nr, nc))
                    for ur, uc in unions:
                        Maps[ur][uc] = peopletotal // len(unions)
        # print(*UnionMaps,sep='\n')
        # print(*Maps, sep='\n')
        # print()
        if count == N*N:
            # print(*Maps, sep='\n')
            break
        else:
            total_count += 1
    print(total_count)