# -*- coding: utf-8 -*-
import copy
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("2573-빙산-1.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())

ocean = [list(map(int, input().split())) for _ in range(N)]

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def new_bing(cr, cc, cb, bingmap):
    bingmap[cr][cc] = cb
    for i in range(4):
        nr, nc = cr + dy[i], cc + dx[i]
        if 0<=nr<N and 0<=nc<M and ocean[nr][nc] and not bingmap[nr][nc]:
            new_bing(nr,nc,cb,bingmap)

def find_alones(ocean):
    bingmap = [[0] * M for _ in range(N)]
    bing = 1
    for r in range(N):
        for c in range(M):
            if ocean[r][c] and not bingmap[r][c]:
                new_bing(r,c,bing, bingmap)
                bing += 1
    return bing - 1

def zero_count(r,c):
    count = 0
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if 0<=nr<N and 0<=nc<M and not ocean[nr][nc]:
            count += 1

    return count

def erosion():
    new_ocean = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if ocean[r][c]:
                new_ocean[r][c] = max(0, ocean[r][c]-zero_count(r,c))
    return new_ocean

time = 0
while True:
    bing_count = find_alones(ocean)
    if bing_count > 1:
        print(time)
        break
    elif bing_count == 0:
        print(0)
        break
    ocean = erosion()
    time += 1
