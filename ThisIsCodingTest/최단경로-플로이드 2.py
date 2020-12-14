import sys

sys.stdin = open("최단경로-플로이드.txt", "r")
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = int(input())
    matrix = [[10e9] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b, d = map(int, input().split())
        matrix[a][b] = min(matrix[a][b],d)
    for r in range(1,N+1):
        for c in range(1,N+1):
            if r == c:
                matrix[r][c] = 0
    for k in range(1,N+1):
        for a in range(1,N+1):
            for b in range(1,N+1):
                matrix[a][b] = min(matrix[a][b],matrix[a][k]+matrix[k][b])
    for r in range(1,N+1):
        for c in range(1,N+1):
            if matrix[r][c] == 10e9: print(0,end=' ')
            else: print(matrix[r][c],end=' ')
        print()