# https://www.acmicpc.net/problem/14502

# https://www.acmicpc.net/source/23910322 이 코드 참고하자
from collections import deque
import sys
import copy
from itertools import combinations

# 밑은 백준용 읽기 코드
# import sys
# input = sys.stdin.readline

sys.stdin = open("DFSBFS-연구소.txt", "r")

def spreadvirus(board):
    viruses = deque()
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 2:
                viruses.append((r,c))
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    while viruses:
        r, c = viruses.popleft()
        board[r][c] = 2
        for i in range(4):
            nr, nc = r+dy[i], c+dx[i]
            if (0<=nr<len(board)) and (0<=nc<len(board[0])) and board[nr][nc] == 0:
                viruses.append((nr,nc))
    return board

def zerocount(board):
    count = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0: count += 1
    return count

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(N)]
    # print(*Map,sep='\n')
    zeros = []
    for r in range(N):
        for c in range(M):
            if Map[r][c] == 0: zeros.append((r,c))
    # print(zeros)
    result = 0
    for comb in combinations(zeros,3):
        tMap = copy.deepcopy(Map)
        for r, c in comb:
            tMap[r][c] = 1
        tMap = spreadvirus(tMap)
        # print(*tMap,sep='\n')
        # print()
        result = max(result,zerocount(tMap))
    print(result)