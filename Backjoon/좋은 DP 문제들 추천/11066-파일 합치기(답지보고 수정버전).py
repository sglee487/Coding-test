# https://www.acmicpc.net/source/28120727
import sys
from collections import defaultdict
MAX = sys.maxsize
sys.stdin = open("11066-파일 합치기-1.txt", "r")

input = sys.stdin.readline

T = int(input())
for test_case in range(T):

    K = int(input())

    pages = list(map(int, input().split()))
    sums = [0]
    for i in pages:
        sums.append(sums[-1] + i)
    # print(pages)
    # print(sums)
    dp = [[0] * K for _ in range(K)]
    for c in range(K-1):
        dp[1][c] = pages[c] + pages[c+1]

    for r in range(2,K):
        for c in range(K-r):
            dp[r][c] = MAX
            for i in range(r):
                if dp[r][c] > (e := dp[r-i-1][c] + dp[i][c+r-i] + (sums[r+c+1]-sums[c])):
                    dp[r][c] = e
        # print(*dp, sep='\n')


    # print(*dp,sep='\n')
    print(dp[-1][0])