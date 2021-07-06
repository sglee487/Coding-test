from collections import deque
import sys

sys.setrecursionlimit(10**9)

sys.stdin = open("3055-탈출-4.txt", "r")

input = sys.stdin.readline

def bfs(forest, waters, S, D):
    global R, C
    distances = [[-1] * C for _ in range(R)]
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    Q = deque()
    Q.append(S)
    distances[S[0]][S[1]] = 0
    while Q:
        lw = len(waters)
        for _ in range(lw):
            r, c = waters.popleft()
            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                if not (0<=nr<R and 0<=nc<C): continue
                if forest[nr][nc] != '.': continue
                forest[nr][nc] = '*'
                waters.append((nr,nc))


        lq = len(Q)
        for _ in range(lq):
            r, c = Q.popleft()
            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                if not (0<=nr<R and 0<=nc<C): continue
                if forest[nr][nc] not in ('.', 'D'): continue
                forest[nr][nc] = 'S'
                distances[nr][nc] = distances[r][c] + 1
                Q.append((nr,nc))
                if (nr,nc) == D:
                    return distances[nr][nc]

    return "KAKTUS"


R, C = map(int, input().split())
forest = [list(input().strip()) for _ in range(R)]
waters = deque()

D = (-1,-1)
S = (-1,-1)
for r in range(R):
    for c in range(C):
        if forest[r][c] == 'D':
            D = (r,c)
        if forest[r][c] == 'S':
            S = (r,c)
        if forest[r][c] == '*':
            waters.append((r,c))

answer = bfs(forest, waters, S, D)
print(answer)