from collections import deque
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("1697-숨바꼭질-1.txt", "r")

def bfs(Q, K):
    global dots, L
    while Q:
        dot, d = Q.popleft()
        if dot == K:
            print(dots)
            return d
        if dot-1 >= 0 and dots[dot-1] == -1:
            dots[dot-1] = d+1
            Q.append((dot-1, d+1))
        if dot+1 <L and dots[dot+1] == -1:
            dots[dot + 1] = d + 1
            Q.append((dot+1, d+1))
        if dot*2 < L and dots[dot*2] == -1:
            dots[dot * 2] = d + 1
            Q.append((dot*2, d+1))

    return 0

input = sys.stdin.readline
N, K = map(int, input().split())
dots = [-1] * 200001
L = len(dots)
Q = deque()
Q.append((N,0))
dots[N] = 1
print(bfs(Q, K))