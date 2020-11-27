from itertools import combinations
import sys

sys.stdin = open("구현-치킨 배달.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # print(*board,sep='\n')
    houses = []
    chickens = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                houses.append((r,c))
            elif board[r][c] == 2:
                chickens.append((r,c))

    # print(chickens)
    mcr = 10e9
    for comc in combinations(chickens, M):
        mr = 0
        for house in houses:
            hd = 10e9
            for chicken in comc:
                hd = min(hd,abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))
            mr += hd
        mcr = min(mr,mcr)
    print(mcr)
    # print()