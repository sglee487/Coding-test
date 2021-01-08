import copy
import sys
from collections import deque

sys.stdin = open("DFSBFS-인구 이동.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def tieunions(sr,sc,UnionMaps, unionindex):
    global L, R, N
    indexunions = [(sr,sc)]
    UnionMaps[sr][sc] = unionindex
    Q = deque()
    Q.append((sr,sc))
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if not (0 <= nr < N and 0 <= nc < N): continue
            if not (L <= abs(Contries[r][c] - Contries[nr][nc]) <= R): continue
            if UnionMaps[nr][nc] != 0: continue
            Q.append((nr,nc))
            UnionMaps[nr][nc] = unionindex
            indexunions.append((nr, nc))
    return indexunions


def getunions(Contries):
    global L, R, N
    unions = []
    unionindex = 1
    UnionMaps = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if UnionMaps[r][c] != 0: continue
            singleunions = tieunions(r,c,UnionMaps,unionindex)
            unionindex += 1
            unions.append(singleunions)
    # print(*UnionMaps,sep='\n')
    return unions, unionindex

T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, L, R = map(int, input().split())
    Contries = [list(map(int, input().split())) for _ in range(N)]
    # print(*Contries,sep='\n')
    tries = 0
    while True:
        unions, unionlen = getunions(Contries)
        if unionlen == ((N*N)+1):
            break
        # print(unions)
        tempContries = copy.deepcopy(Contries)
        for i in range(unionlen-1):
            peopletotal = 0
            for r, c in unions[i]:
                peopletotal += Contries[r][c]

            for r, c in unions[i]:
                tempContries[r][c] = peopletotal // len(unions[i])
        Contries = copy.deepcopy(tempContries)
        # print(*Contries, sep='\n')
        tries += 1
    print(tries)