
import sys

sys.stdin = open("DP-정수 삼각형.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tri = [[0] * (N+1) for _ in range(N)]
    for r in range(N):
        temp = list(map(int, input().split()))
        for c,t in enumerate(temp):
            tri[r][c+1] = t
    # print(*tri,sep='\n')
    trisum = [[0] * (N+1) for _ in range(N)]
    trisum[0][1] = tri[0][1]
    for r in range(1,N):
        for c in range(1,r+2):
            trisum[r][c] = max(trisum[r-1][c-1],trisum[r-1][c]) + tri[r][c]

    # print(*trisum,sep='\n')
    print(max(trisum[-1]))