import sys
from collections import defaultdict

sys.stdin = open("11066-파일 합치기-1.txt", "r")

input = sys.stdin.readline


T = int(input())
for test_case in range(T):
    K = int(input())
    pages = list(map(int, input().split()))
    # print(sum(pages))
    matrix = [[0] * K for _ in range(K)]
    dp = [[0] * K for _ in range(K)]
    matrix[0] = pages
    dp[0] = pages
    for r in range(1,K):
        for c in range(K-r):
            for i in range(r):
                total = matrix[r-i-1][c] + matrix[i][r-i+c]
                if matrix[r][c] == 0 or total < matrix[r][c]:
                    matrix[r][c] = total

    for r in range(1,K):
        for c in range(K-r):
            for i in range(r):
                total = matrix[r][c]
                if r-i-1 != 0:
                    total += dp[r-i-1][c]
                if i != 0:
                    total += dp[i][r-i+c]
                if dp[r][c] == 0 or total < dp[r][c]:
                    dp[r][c] = total


    print(*matrix,sep='\n')
    print(*dp,sep='\n')
    # print(2011,1016)
    print(dp[K-1][0])