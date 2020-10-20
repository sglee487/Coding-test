import sys

sys.stdin = open("DP-금광.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    al = list(map(int, input().split()))
    gold = [[0] * (M+2) for _ in range(N+2)]
    for i in range(len(al)):
        gold[(i//M)+1][(i%M)+1] = al[i]
    print(*gold,sep='\n')
    earngold = [[0] * (M+2) for _ in range(N+2)]
    for i in range(N):
        earngold[i+1][1] = gold[i+1][1]
    result = 0
    for c in range(2,M+1):
        for r in range(1,N+1):
            earngold[r][c] = max(earngold[r-1][c-1],earngold[r][c-1],earngold[r+1][c-1]) + gold[r][c]
            result = max(result,earngold[r][c])
    print(*earngold, sep='\n')
    print(result)