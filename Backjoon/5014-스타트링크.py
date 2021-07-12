import sys
sys.setrecursionlimit(10**9)
from collections import deque


sys.stdin = open("5014-스타트링크-1.txt", "r")

input = sys.stdin.readline

def bfs(Q, floors):
    global F, S, G, U, D
    while Q:
        f, d = Q.popleft()
        if f == G:
            return d
        if f+U <= F and floors[f+U] == -1:
            floors[f+U] = d+1
            Q.append((f+U,d+1))
        if f-D >= 1 and floors[f-D] == -1:
            floors[f - D] = d + 1
            Q.append((f-D,d+1))

    return "use the stairs"

F, S, G, U, D = map(int, input().split())
floors = [-1] * (F+1)
Q = deque()
Q.append((S,0))
floors[S] = 0
print(bfs(Q, floors))