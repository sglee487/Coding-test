from collections import deque
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("ARCTIC-1.txt", "r")

input = sys.stdin.readline

def distance(x1,y1,x2,y2):
    return (abs(x1-x2)**2 + abs(y1-y2)**2) ** (1/2)


def canAllConnected(N, bases, transDistance):
    Q = deque()
    Q.append(0)
    visited = [False] * N
    visited[0] = True
    count = 1
    while Q:
        now = Q.popleft()
        x1, y1 = bases[now]
        for next in range(N):
            x2, y2 = bases[next]
            if not visited[next] and distance(x1,y1,x2,y2) <= transDistance:
                visited[next] = True
                Q.append(next)
                count += 1
    return N==count

def solve(N, bases):

    lo, hi = 0., 1415.
    for _ in range(100):
        mid = (lo + hi) / 2
        if canAllConnected(N,bases,mid):
            hi = mid
        else:
            lo = mid
    return lo


C = int(input())
for _ in range(C):
    N = int(input())
    bases = [tuple(map(float, input().split())) for _ in range(N)]
    print(f"{solve(N, bases):.2f}")