from itertools import combinations
import sys

sys.stdin = open("구현-치킨 배달.txt", "r")
input = sys.stdin.readline # 꼭 sys.stdin 밑에

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    Maps = [list(map(int, input().split())) for _ in range(N)]
    # print(*Maps,sep='\n')
    houses = []
    chickens = []
    for r in range(N):
        for c in range(N):
            if Maps[r][c] == 1:
                houses.append((r,c))
            elif Maps[r][c] == 2:
                chickens.append((r,c))
    # print(houses)
    # print(chickens)
    Mcitystreet = int(10e9)
    for comb in combinations(chickens,M):
        citystreet = 0
        for house in houses:
            housestreet = int(10e9)
            for chicken in comb:
                housestreet = min(housestreet,abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))
            citystreet += housestreet
        Mcitystreet = min(Mcitystreet,citystreet)
    print(Mcitystreet)