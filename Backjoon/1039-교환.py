from collections import deque

import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("1039-교환-2.txt", "r")

def swap(n,i,j, M) -> int:
    num = n
    ni = n % (10 ** i) // (10 ** (i-1))
    nj = n % (10 ** j) // (10 ** (j-1))
    if j == M and ni == 0:
        return False
    num -= ni * (10 ** (i-1))
    num -= nj * (10 ** (j-1))
    num += ni * (10 ** (j-1))
    num += nj * (10 ** (i-1))

    return num

def bfs(N,K):
    dp = [0] * (1000001)
    Q = deque()
    M = len(str(N))
    Q.append((N,0))
    dp[N] = 0
    answer = -1
    while Q:
        n, d = Q.popleft()
        if d == K:
            if n > answer:
                answer = n
            continue
        for i in range(1, M+1):
            for j in range(i+1, M+1):
                num = swap(n, i, j, M)
                if not num:
                    continue
                if dp[num] != d+1:
                    dp[num] = d+1
                    Q.append((num, d+1))
    return answer

input = sys.stdin.readline

N, K = map(int, input().split())

print(bfs(N,K))