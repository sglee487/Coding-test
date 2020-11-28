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
    while viruses:
        r, c = viruses.popleft()
        board[r][c] = 2
        # 위
        if 0 <= r - 1 and board[r - 1][c] == 0:
            viruses.append((r-1,c))
        # 오른쪽
        if c + 1 < len(board[0]) and board[r][c + 1] == 0:
            viruses.append((r,c+1))
        # 아래
        if r + 1 < len(board) and board[r + 1][c] == 0:
            board[r + 1][c] = 2
            viruses.append((r+1,c))
        # 왼쪽
        if 0 <= c - 1 and board[r][c - 1] == 0:
            board[r][c - 1] = 2
            viruses.append((r,c-1))
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