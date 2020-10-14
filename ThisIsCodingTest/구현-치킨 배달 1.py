from itertools import combinations

import sys

sys.stdin = open("구현-치킨 배달.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    # print(*board,sep='\n')
    housel = []
    chickenl = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                housel.append((r,c))
            elif board[r][c] == 2:
                chickenl.append((r,c))
    shorestotald = N**3
    for cl in combinations(chickenl,M):
        ptd = 0
        for hr, hc in housel:
            shd = N*2
            for cr, cc in cl:
                if abs(hr-cr) + abs(hc-cc) < shd:
                    shd = abs(hr-cr) + abs(hc-cc)
            ptd += shd
        if ptd < shorestotald:
            shorestotald = ptd
    print(shorestotald)