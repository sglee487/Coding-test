import sys
from collections import deque

sys.stdin = open("9019-DSLR-2.txt", "r")

input = sys.stdin.readline

def bfs(Q, A, B):
    while Q:
        n, s = Q.popleft()
        e = (2*n) % 10000
        if dp[e] == False:
            dp[e] = True
            if e == B:
                return s + 'D'
            Q.append((e, s + 'D'))
        f = (n-1)%10000
        if dp[f] == False:
            dp[f] = True
            if f == B:
                return s + 'S'
            Q.append((f, s + 'S'))
        g = 10*(n%1000)+n//1000
        if dp[g] == False:
            dp[g] = True
            if g == B:
                return s + 'L'
            Q.append((g, s + 'L'))
        h = 1000*(n%10)+n//10
        if dp[h] == False:
            dp[h] = True
            if h == B:
                return s + 'R'
            Q.append((h, s + 'R'))

T = int(input())
for test_case in range(T):
    A, B = map(int, input().split())
    dp = [False] * (10001)
    Q = deque()
    Q.append((A,''))
    print(bfs(Q, A, B))